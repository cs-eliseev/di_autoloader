from typing import Dict, Any, Callable
from di_autoloader import ContainerWrapper, ContainerFactory

class ContainerAutoloader:
    _instance = None

    @classmethod
    def get_instance(
            cls,
            instance: str = 'default',
            configuration: Dict[str, Any] | None = None,
            configs: Dict[str, Any] = None,
            init: bool = True,
    ) -> ContainerWrapper:
        if cls._instance[instance] is None:
            cls._instance[instance] = ContainerFactory.make_container(configuration, configs)
            if init:
                cls._instance[instance].init_resources()
        return cls._instance[instance]

    @classmethod
    def get_instance_by_callable(
            cls,
            configuration_function: Callable[[], None],
            configs_function: Callable[[], None],
            instance: str = 'default',
            init: bool = True,
    ) -> ContainerWrapper:
        return cls.get_instance(instance, configuration_function(), configs_function(), init)