from examples.resources.src.container_test_init import container_init

# Инициализация контейнера
container = container_init({}, {'settings': {'key': 'this config'}})

print(container.config.get('settings.key'))