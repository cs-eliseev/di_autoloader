from di_autoloader.container_autoloader import ContainerAutoloader

container = ContainerAutoloader.get_instance(
    configuration={
        'sum_object': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs_factory': {'config': 'object'},
        },
        'sum_object_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs_factory': {'config': 'object'},
        },
        'sum_aggregate': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs_factory': {
                'sum_object__1': {
                    'sum_object': {'container': 'sum_object__1'},
                },
                'sum_object__2': {
                    'sum_object': {'container': 'sum_object__2'}
                },
            },
        },
        'sum_aggregate2': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs_factory': {
                'sum_object_s__1': {
                    'sum_object': {'container': 'sum_object_s__1'},
                },
                'sum_object_s__2': {
                    'sum_object': {'container': 'sum_object_s__2'}
                },
            },
        },
        'sum_aggregate_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs_factory': {
                'sum_object__1': {
                    'sum_object': {'container': 'sum_object__1'},
                },
                'sum_object__2': {
                    'sum_object': {'container': 'sum_object__2'}
                },
            },
        },
        'sum_aggregate_s2': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs_factory': {
                'sum_object_s__1': {
                    'sum_object': {'container': 'sum_object_s__1'},
                },
                'sum_object_s__2': {
                    'sum_object': {'container': 'sum_object_s__2'}
                },
            },
        },
    },
    configs={
        'object': {
            '1': {
                'a': 4,
                'b': 4
            },
            '2': {
                'a': 4,
                'b': 5
            },
        }
    }
)

print(f"sum_aggregate__sum_object__1: {container.sum_aggregate__sum_object__1().sum()}")
print(f"sum_aggregate__sum_object__2: {container.sum_aggregate__sum_object__2().sum()}")
print(f"sum_aggregate2__sum_object_s__1: {container.sum_aggregate2__sum_object_s__1().sum()}")
print(f"sum_aggregate2__sum_object_s__2: {container.sum_aggregate2__sum_object_s__2().sum()}")
print(f"sum_aggregate_s__sum_object__1: {container.sum_aggregate_s__sum_object__1().sum()}")
print(f"sum_aggregate_s__sum_object__2: {container.sum_aggregate_s__sum_object__2().sum()}")
print(f"sum_aggregate_s2__sum_object_s__1: {container.sum_aggregate_s2__sum_object_s__1().sum()}")
print(f"sum_aggregate_s2__sum_object_s__2: {container.sum_aggregate_s2__sum_object_s__2().sum()}")

print(f"sum_aggregate__sum_object__1 === sum_aggregate__sum_object__1 ? {container.sum_aggregate__sum_object__1() is container.sum_aggregate__sum_object__1()}")
print(f"sum_aggregate__sum_object__1 === sum_aggregate__sum_object__2 ? {container.sum_aggregate__sum_object__1() is container.sum_aggregate__sum_object__2()}")
print(f"sum_aggregate__sum_object__1 === sum_aggregate2__sum_object_s__1 ? {container.sum_aggregate__sum_object__1() is container.sum_aggregate2__sum_object_s__1()}")
print(f"sum_aggregate__sum_object__1 === sum_aggregate2__sum_object_s__2 ? {container.sum_aggregate__sum_object__1() is container.sum_aggregate2__sum_object_s__2()}")
print(f"sum_aggregate__sum_object__1 === sum_aggregate_s__sum_object__1 ? {container.sum_aggregate__sum_object__1() is container.sum_aggregate_s__sum_object__1()}")
print(f"sum_aggregate__sum_object__1 === sum_aggregate_s__sum_object__2 ? {container.sum_aggregate__sum_object__1() is container.sum_aggregate_s__sum_object__2()}")
print(f"sum_aggregate__sum_object__1 === sum_aggregate_s2__sum_object_s__1 ? {container.sum_aggregate__sum_object__1() is container.sum_aggregate_s2__sum_object_s__1()}")
print(f"sum_aggregate__sum_object__1 === sum_aggregate_s2__sum_object_s__2 ? {container.sum_aggregate__sum_object__1() is container.sum_aggregate_s2__sum_object_s__2()}")

print(f"sum_aggregate__sum_object__2 === sum_aggregate__sum_object__2 ? {container.sum_aggregate__sum_object__2() is container.sum_aggregate__sum_object__2()}")
print(f"sum_aggregate__sum_object__2 === sum_aggregate2__sum_object_s__1 ? {container.sum_aggregate__sum_object__2() is container.sum_aggregate2__sum_object_s__1()}")
print(f"sum_aggregate__sum_object__2 === sum_aggregate2__sum_object_s__2 ? {container.sum_aggregate__sum_object__2() is container.sum_aggregate2__sum_object_s__2()}")
print(f"sum_aggregate__sum_object__2 === sum_aggregate_s__sum_object__1 ? {container.sum_aggregate__sum_object__2() is container.sum_aggregate_s__sum_object__1()}")
print(f"sum_aggregate__sum_object__2 === sum_aggregate_s__sum_object__2 ? {container.sum_aggregate__sum_object__2() is container.sum_aggregate_s__sum_object__2()}")
print(f"sum_aggregate__sum_object__2 === sum_aggregate_s2__sum_object_s__1 ? {container.sum_aggregate__sum_object__2() is container.sum_aggregate_s2__sum_object_s__1()}")
print(f"sum_aggregate__sum_object__2 === sum_aggregate_s2__sum_object_s__2 ? {container.sum_aggregate__sum_object__2() is container.sum_aggregate_s2__sum_object_s__2()}")

print(f"sum_aggregate2__sum_object_s__1 === sum_aggregate2__sum_object_s__1 ? {container.sum_aggregate2__sum_object_s__1() is container.sum_aggregate2__sum_object_s__1()}")
print(f"sum_aggregate2__sum_object_s__1 === sum_aggregate2__sum_object_s__2 ? {container.sum_aggregate2__sum_object_s__1() is container.sum_aggregate2__sum_object_s__2()}")
print(f"sum_aggregate2__sum_object_s__1 === sum_aggregate_s__sum_object__1 ? {container.sum_aggregate2__sum_object_s__1() is container.sum_aggregate_s__sum_object__1()}")
print(f"sum_aggregate2__sum_object_s__1 === sum_aggregate_s__sum_object__2 ? {container.sum_aggregate2__sum_object_s__1() is container.sum_aggregate_s__sum_object__2()}")
print(f"sum_aggregate2__sum_object_s__1 === sum_aggregate_s2__sum_object_s__1 ? {container.sum_aggregate2__sum_object_s__1() is container.sum_aggregate_s2__sum_object_s__1()}")
print(f"sum_aggregate2__sum_object_s__1 === sum_aggregate_s2__sum_object_s__2 ? {container.sum_aggregate2__sum_object_s__1() is container.sum_aggregate_s2__sum_object_s__2()}")

print(f"sum_aggregate2__sum_object_s__2 === sum_aggregate2__sum_object_s__2 ? {container.sum_aggregate2__sum_object_s__2() is container.sum_aggregate2__sum_object_s__2()}")
print(f"sum_aggregate2__sum_object_s__2 === sum_aggregate_s__sum_object__1 ? {container.sum_aggregate2__sum_object_s__2() is container.sum_aggregate_s__sum_object__1()}")
print(f"sum_aggregate2__sum_object_s__2 === sum_aggregate_s__sum_object__2 ? {container.sum_aggregate2__sum_object_s__2() is container.sum_aggregate_s__sum_object__2()}")
print(f"sum_aggregate2__sum_object_s__2 === sum_aggregate_s2__sum_object_s__1 ? {container.sum_aggregate2__sum_object_s__2() is container.sum_aggregate_s2__sum_object_s__1()}")
print(f"sum_aggregate2__sum_object_s__2 === sum_aggregate_s2__sum_object_s__2 ? {container.sum_aggregate2__sum_object_s__2() is container.sum_aggregate_s2__sum_object_s__2()}")

print(f"sum_aggregate_s__sum_object__1 === sum_aggregate_s__sum_object__1 ? {container.sum_aggregate_s__sum_object__1() is container.sum_aggregate_s__sum_object__1()}")
print(f"sum_aggregate_s__sum_object__1 === sum_aggregate_s__sum_object__2 ? {container.sum_aggregate_s__sum_object__1() is container.sum_aggregate_s__sum_object__2()}")
print(f"sum_aggregate_s__sum_object__1 === sum_aggregate_s2__sum_object_s__1 ? {container.sum_aggregate_s__sum_object__1() is container.sum_aggregate_s2__sum_object_s__1()}")
print(f"sum_aggregate_s__sum_object__1 === sum_aggregate_s2__sum_object_s__2 ? {container.sum_aggregate_s__sum_object__1() is container.sum_aggregate_s2__sum_object_s__2()}")

print(f"sum_aggregate_s__sum_object__2 === sum_aggregate_s__sum_object__2 ? {container.sum_aggregate_s__sum_object__2() is container.sum_aggregate_s__sum_object__2()}")
print(f"sum_aggregate_s__sum_object__2 === sum_aggregate_s2__sum_object_s__1 ? {container.sum_aggregate_s__sum_object__2() is container.sum_aggregate_s2__sum_object_s__1()}")
print(f"sum_aggregate_s__sum_object__2 === sum_aggregate_s2__sum_object_s__2 ? {container.sum_aggregate_s__sum_object__2() is container.sum_aggregate_s2__sum_object_s__2()}")

print(f"sum_aggregate_s2__sum_object_s__1 === sum_aggregate_s2__sum_object_s__1 ? {container.sum_aggregate_s2__sum_object_s__1() is container.sum_aggregate_s2__sum_object_s__1()}")
print(f"sum_aggregate_s2__sum_object_s__1 === sum_aggregate_s2__sum_object_s__2 ? {container.sum_aggregate_s2__sum_object_s__1() is container.sum_aggregate_s2__sum_object_s__2()}")

print(f"sum_aggregate_s2__sum_object_s__2 === sum_aggregate_s2__sum_object_s__2 ? {container.sum_aggregate_s2__sum_object_s__2() is container.sum_aggregate_s2__sum_object_s__2()}")