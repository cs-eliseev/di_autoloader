from typing import Dict, Any, Callable
from di_autoloader import ContainerWrapper, ContainerFactory

class ContainerAutoloader:
    _instance = {}

    @classmethod
    def get_instance(
            cls,
            configuration: Dict[str, Any] | None = None,
            configs: Dict[str, Any] = None,
            instance: str = 'default',
            init: bool = True,
    ) -> ContainerWrapper:
        if instance not in cls._instance:
            cls._instance[instance] = ContainerFactory.make_container(configuration=configuration, configs=configs)
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
        if instance not in cls._instance:
            return cls.get_instance(
                instance=instance,
                configuration=configuration_function(),
                configs=configs_function(),
                init=init
            )
        return cls._instance[instance]