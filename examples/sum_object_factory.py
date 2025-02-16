from examples.resources.src.container_test_init import container_init

container = container_init(
    {
        'sum_object': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs_config': 'settings',
        },
        'sum_object_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs_config': 'settings',
        },
    }, {
        'settings': {
            '1': {
                'a': 3,
                'b': 3
            },
            '2': {
                'a': 3,
                'b': 4
            },
        }
    }
)

print(f"sum_object__1: {container.sum_object__1().sum()}")
print(f"sum_object__2: {container.sum_object__2().sum()}")
print(f"sum_object_s__1: {container.sum_object_s__1().sum()}")
print(f"sum_object_s__2: {container.sum_object_s__2().sum()}")

print(f"sum_object__1 === sum_object__1 ? {container.sum_object__1() is container.sum_object__1()}")
print(f"sum_object__1 === sum_object__2 ? {container.sum_object__1() is container.sum_object__2()}")
print(f"sum_object__1 === sum_object_s__1 ? {container.sum_object__1() is container.sum_object_s__1()}")
print(f"sum_object__1 === sum_object_s__2 ? {container.sum_object__1() is container.sum_object_s__2()}")
print(f"sum_object__2 === sum_object__2 ? {container.sum_object__2() is container.sum_object__2()}")
print(f"sum_object__2 === sum_object_s__1 ? {container.sum_object__2() is container.sum_object_s__1()}")
print(f"sum_object__2 === sum_object_s__2 ? {container.sum_object__2() is container.sum_object_s__2()}")
print(f"sum_object_s__1 === sum_object_s__1 ? {container.sum_object_s__1() is container.sum_object_s__1()}")
print(f"sum_object_s__1 === sum_object_s__2 ? {container.sum_object_s__1() is container.sum_object_s__2()}")
print(f"sum_object_s__2 === sum_object_s__2 ? {container.sum_object_s__2() is container.sum_object_s__2()}")