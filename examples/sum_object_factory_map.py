from di_autoloader.container_autoloader import ContainerAutoloader

container = ContainerAutoloader.get_instance(
    configuration={
        'sum_object': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs_factory': {
                '1': {
                    'a': 3,
                    'b': 5
                },
                '2': {
                    'a': 3,
                    'b': 6
                },
            },
        },
        'sum_object_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs_factory': {
                '1': {
                    'a': 3,
                    'b': 5
                },
                '2': {
                    'a': 3,
                    'b': 6
                },
            },
        },
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