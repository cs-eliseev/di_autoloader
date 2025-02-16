from typing import Dict, Any
from di_autoloader.container_loader import DIContainerLoader
from di_autoloader.container_wrapper import ContainerWrapper
from di_autoloader.dependency_resolver import DependencyResolver
from di_autoloader.provider_factory import ProviderFactory

class ContainerFactory:
    @staticmethod
    def make_container(configuration: Dict[str, Any]|None = None, configs: Dict[str, Any] = None) -> ContainerWrapper:
        container = ContainerWrapper()

        if configs is not None:
            container.config.from_dict(configs)

        if configuration is not None:
            loader = DIContainerLoader(container, ProviderFactory(container, DependencyResolver(container)))
            loader.load(configuration)

        return container