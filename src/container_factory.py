from typing import Dict, Any
from src.container_loader import DIContainerLoader
from src.container_wrapper import ContainerWrapper
from src.dependency_resolver import DependencyResolver
from src.provider_factory import ProviderFactory

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