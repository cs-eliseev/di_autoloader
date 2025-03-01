from di_autoloader.container_autoloader import ContainerAutoloader

a = 4
b = 1

container = ContainerAutoloader.get_instance(
    configuration={
        'sum_object': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs': {
                'a': a,
                'b': b
            }
        },
        'sum_object_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_object.SumObject',
            'kwargs': {
                'a': a,
                'b': b
            }
        },
        'sum_aggregate__so': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs': {
                'sum_object': {'container': 'sum_object'}
            }
        },
        'sum_aggregate__so_s': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs': {
                'sum_object': {'container': 'sum_object_s'}
            }
        },
        'sum_aggregate_s__so': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs': {
                'sum_object': {'container': 'sum_object'}
            }
        },
        'sum_aggregate_s__so_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_aggregate.SumAggregate',
            'kwargs': {
                'sum_object': {'container': 'sum_object_s'}
            }
        },
    }
)

print(f"sum_aggregate__so: {container.sum_aggregate__so().sum()}")
print(f"sum_aggregate__so_s: {container.sum_aggregate__so_s().sum()}")
print(f"sum_aggregate_s__so: {container.sum_aggregate_s__so().sum()}")
print(f"sum_aggregate_s__so_s: {container.sum_aggregate_s__so_s().sum()}")

print(f"sum_aggregate__so === sum_aggregate__so ? {container.sum_aggregate__so() is container.sum_aggregate__so()}")
print(f"sum_aggregate__so === sum_aggregate__so_s ? {container.sum_aggregate__so() is container.sum_aggregate__so_s()}")
print(f"sum_aggregate__so === sum_aggregate_s__so ? {container.sum_aggregate__so() is container.sum_aggregate_s__so()}")
print(f"sum_aggregate__so === sum_aggregate_s__so_s ? {container.sum_aggregate__so() is container.sum_aggregate_s__so_s()}")
print(f"sum_aggregate__so_s === sum_aggregate__so_s ? {container.sum_aggregate__so_s() is container.sum_aggregate__so_s()}")
print(f"sum_aggregate__so_s === sum_aggregate_s__so ? {container.sum_aggregate__so_s() is container.sum_aggregate_s__so()}")
print(f"sum_aggregate__so_s === sum_aggregate_s__so_s ? {container.sum_aggregate__so_s() is container.sum_aggregate_s__so_s()}")
print(f"sum_aggregate_s__so === sum_aggregate_s__so ? {container.sum_aggregate_s__so() is container.sum_aggregate_s__so()}")
print(f"sum_aggregate_s__so === sum_aggregate_s__so_s ? {container.sum_aggregate_s__so() is container.sum_aggregate_s__so_s()}")
print(f"sum_aggregate_s__so_s === sum_aggregate_s__so_s ? {container.sum_aggregate_s__so_s() is container.sum_aggregate_s__so_s()}")