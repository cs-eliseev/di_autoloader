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

        # kwargs_factory Handler
        if 'kwargs_factory' in config and isinstance(config['kwargs_factory'], dict):
            kwargs_map = self._prepare_kwargs_factory(config['kwargs_factory'])
            return self._make_providers_kwargs_map(
                name=name,
                kwargs_map=kwargs_map,
                provider_type=provider_type,
                instance=instance
            )

        if config.get('provider') == 'Delegate':
            return {name: provider_type(lambda: instance(**kwargs))}

        # Обычное создание провайдера
        return {name: self._make_base_provider(provider_type=provider_type, instance=instance, kwargs=kwargs)}

    @staticmethod
    def _make_base_provider(provider_type, instance, kwargs) -> Any:
        return provider_type(instance, **kwargs) if instance else provider_type(**kwargs)

    def _make_providers_kwargs_map(self, name: str, kwargs_map: Dict[str, Any], provider_type, instance) -> dict[str, Any]:
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

    def _prepare_kwargs_factory(self, kwargs_data: dict[str, Any]) -> dict:
        # get from container config
        if 'config' in kwargs_data:
            kwargs_map = self.resolver.resolve(kwargs_data)
            if not isinstance(kwargs_map, dict):
                raise KwargsMapUndefined(kwargs_map)
            return kwargs_map

        return kwargs_data