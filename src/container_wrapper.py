from dependency_injector import containers, providers

class ContainerWrapper(containers.DeclarativeContainer):
    config = providers.Configuration()