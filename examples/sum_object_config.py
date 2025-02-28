from di_autoloader.container_autoloader import ContainerAutoloader

container = ContainerAutoloader.get_instance(
    configuration={
        'sum_object': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs': {
                'a': {'config': 'settings.a'},
                'b': {'config': 'settings.b'}
            }
        },
        'sum_object_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs': {
                'a': {'config': 'settings.a'},
                'b': {'config': 'settings.b'}
            }
        }
    },
    configs={
        'settings': {
            'a': 3,
            'b': 2,
        }
    }
)

print(f"sum_object: {container.sum_object().sum()}")
print(f"sum_object_s: {container.sum_object_s().sum()}")

print(f"sum_object === sum_object ? {container.sum_object() is container.sum_object()}")
print(f"sum_object === sum_object_s ? {container.sum_object() is container.sum_object_s()}")
print(f"sum_object_s === sum_object_s ? {container.sum_object_s() is container.sum_object_s()}")