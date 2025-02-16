from examples.resources.src.container_test_init import container_init

container = container_init(
    {
        'sum_object': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs_config': 'object',
        },
        'sum_object_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs_config': 'object',
        },
        'sum_aggregate': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs_config': 'aggregate',
        },
        'sum_aggregate2': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs_config': 'aggregate_s',
        },
        'sum_aggregate_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs_config': 'aggregate',
        },
        'sum_aggregate_s2': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs_config': 'aggregate_s',
        },
    }, {
        'object': {
            '1': {
                'a': 4,
                'b': 2
            },
            '2': {
                'a': 4,
                'b': 4
            },
        },
        'aggregate': {
            'sum_object__1': {
                'sum_object': {'container': 'sum_object__1'},
            },
            'sum_object__2': {
                'sum_object': {'container': 'sum_object__2'}
            },
        },
        'aggregate_s': {
            'sum_object_s__1': {
                'sum_object': {'container': 'sum_object_s__1'},
            },
            'sum_object_s__2': {
                'sum_object': {'container': 'sum_object_s__2'}
            },
        },
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