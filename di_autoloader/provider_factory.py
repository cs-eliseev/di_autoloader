import importlib
from typing import Any, Dict
from dependency_injector import providers, containers
from di_autoloader.dependency_resolver import DependencyResolver

class ProviderNotFound(ValueError):
    def __init__(self, provider: str) -> None:
        super().__init__(f"Provider '{provider}' not found.")

class ClassImportFailed(ImportError):
    def __init__(self, class_path: str, error) -> None:
        super().__init__(f"Class '{class_path}' import failed! {error}")

class KwargsMapUndefined(ValueError):
    def __init__(self, kwargs_map: Any) -> None:
        super().__init__(f"Expected a dictionary for 'kwargs_map', got: {type(kwargs_map)}")

class KwargsUndefined(ValueError):
    def __init__(self, kwargs_map: Any) -> None:
        super().__init__(f"Expected a dictionary for 'kwargs', got: {type(kwargs_map)}")

class ProviderFactory:
    """Фабрика для создания провайдеров из конфигурации."""
    PROVIDER_MAP = {
        'Configuration': providers.Configuration,
        'Factory': providers.Factory,
        'Singleton': providers.Singleton,
        'Delegate': providers.Delegate,
    }

    def __init__(
            self,
            container: containers.DeclarativeContainer,
            resolver: DependencyResolver,
            custom_providers: dict[str, type] = None
    ) -> None:
        self.container = container
        self.resolver = resolver
        if custom_providers is not None:
            self.PROVIDER_MAP.update(custom_providers)

    @staticmethod
    def import_class(class_path: str):
        try:
            module_name, class_name = class_path.rsplit('.', 1)
            module = importlib.import_module(module_name)
            return getattr(module, class_name)
        except (ImportError, AttributeError) as e:
            raise ClassImportFailed(class_path, e)

    def create_provider(self, name: str, config: Dict[str, Any]) -> Any:
        provider_type = self.PROVIDER_MAP.get(config.get('provider'))
        if not provider_type:
            raise ProviderNotFound(config.get('provider'))
        instance = self.import_class(class_path=config['provides']) if 'provides' in config else None
        kwargs = {k: self.resolver.resolve(value=v) for k, v in config.get('kwargs', {}).items()}

        # kwargs_map Handler
        if 'kwargs_config' in config:
            return self._make_providers_kwargs_config(
                name=name,
                config=config,
                provider_type=provider_type,
                instance=instance
            )

        # kwargs_factory Handler (NOT USED)
        if 'kwargs_factory' in config:
            return self._make_providers_kwargs_factory(
                name=name,
                config=config,
                provider_type=provider_type,
                instance=instance
            )

        if config.get('provider') == 'Delegate':
            return {'name': provider_type(lambda: instance(**kwargs))}

        # Обычное создание провайдера
        return {'name': self._make_base_provider(provider_type=provider_type, instance=instance, kwargs=kwargs)}

    @staticmethod
    def _make_base_provider(provider_type, instance, kwargs) -> Any:
        return provider_type(instance, **kwargs) if instance else provider_type(**kwargs)

    def _make_providers_kwargs_config(self, name: str, config: Dict[str, Any], provider_type, instance) -> dict[str, Any]:
        kwargs_map = self.resolver.resolve({'config': config['kwargs_config']})
        if not isinstance(kwargs_map, dict):
            raise KwargsMapUndefined(kwargs_map)
        items = {}
        for key, kwargs in kwargs_map.items():
            if not isinstance(kwargs, dict):
                raise KwargsUndefined(kwargs)
            items[f"{name}__{key}"] = self._make_base_provider(
                provider_type=provider_type,
                instance=instance,
                kwargs=self.resolver.resolve(value=kwargs)
            )
        return items

    def _make_providers_kwargs_factory(self, name: str, config: Dict[str, Any], provider_type, instance) -> dict[str, Any]:
        kwargs_factories = {k: self.resolver.resolve(value=v) for k, v in config['kwargs_factory'].items()}
        items = {}
        for key, factory_name in kwargs_factories.items():
            if not hasattr(self.container, factory_name):
                raise Exception(f"Factory provider '{factory_name}' not found in container.")
            items[f"{name}__{key}"] = provider_type(instance, **{key: getattr(self.container, factory_name)})
        return items
