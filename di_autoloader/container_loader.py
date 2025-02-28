from typing import Any, Dict
from dependency_injector import containers
from di_autoloader.provider_factory import ProviderFactory

class ConfigurationDependencyIncorrect(ValueError):
    def __init__(self, name: str) -> None:
        super().__init__(f"Configuration dependency '{name}' is incorrect")

class CreatingProviderFailed(RuntimeError):
    def __init__(self, name: str, error) -> None:
        super().__init__(f"Provider '{name}' was not created: {error}")

class DIContainerLoader:
    """Класс для загрузки зависимостей в DI-контейнер."""
    def __init__(self, container: containers.DeclarativeContainer, provider_factory: ProviderFactory) -> None:
        self.container = container
        self.provider_factory = provider_factory

    def load(self, configs: Dict[str, Any]) -> None:
        for name, config in configs.items():
            if not isinstance(config, dict):
                raise ConfigurationDependencyIncorrect(name=name)
            try:
                self._load_map(self.provider_factory.create_provider(name=name, config=config))
            except Exception as e:
                raise CreatingProviderFailed(name=name, error=e)

    def _load_map(self, providers: dict):
        for name, provider in providers.items():
            setattr(self.container, name, provider)