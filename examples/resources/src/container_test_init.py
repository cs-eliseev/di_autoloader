from typing import Dict, Any
from di_autoloader.container_factory import ContainerFactory
from di_autoloader.container_wrapper import ContainerWrapper

def container_init(dataset: Dict[str, Any] = None, configs: Dict[str, Any] = None) -> ContainerWrapper:
    container = ContainerFactory.make_container(dataset, configs)

    # Использование загруженных зависимостей
    container.init_resources()

    return container