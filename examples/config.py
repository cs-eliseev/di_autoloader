from di_autoloader.container_autoloader import ContainerAutoloader

container = ContainerAutoloader.get_instance(configs={'settings': {'key': 'this config'}})
print(container.config.get('settings.key'))