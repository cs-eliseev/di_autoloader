from typing import Dict, Any
from src.container_factory import ContainerFactory
from src.container_wrapper import ContainerWrapper

def container_init(dataset: Dict[str, Any] = None, configs: Dict[str, Any] = None) -> ContainerWrapper:
    container = ContainerFactory.make_container(dataset, configs)

    # Использование загруженных зависимостей
    container.init_resources()

    return container