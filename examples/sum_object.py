from examples.resources.src.container_test_init import container_init

a = 3
b = 1

container = container_init(
    {
        'sum_object': {
            'provider': 'Factory',
            'provides': 'examples.resources.di_autoloader.sum_object.SumObject',
            'kwargs': {
                'a': a,
                'b': b
            }
        },
        'sum_object_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.di_autoloader.sum_object.SumObject',
            'kwargs': {
                'a': a,
                'b': b
            }
        }
    }
)

print(f"sum_object: {container.sum_object().sum()}")
print(f"sum_object_s: {container.sum_object_s().sum()}")

print(f"sum_object === sum_object ? {container.sum_object() is container.sum_object()}")
print(f"sum_object === sum_object_s ? {container.sum_object() is container.sum_object_s()}")
print(f"sum_object_s === sum_object_s ? {container.sum_object_s() is container.sum_object_s()}")