from di_autoloader.container_autoloader import ContainerAutoloader

container = ContainerAutoloader.get_instance(
    configuration={
        'sum_handler': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_handler.SumHandler'
        },
        'sum_handler_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_handler.SumHandler'
        },
        'sum_wrapper': {
            'provider': 'Factory',
            'provides': 'examples.resources.src.sum_wrapper.SumWrapper',
            'kwargs_factory': {
                'sh': {
                    'handler': {'container': 'sum_handler'}
                },
                'sh_s': {
                    'handler': {'container': 'sum_handler_s'}
                },
            }
        },
        'sum_wrapper_s': {
            'provider': 'Singleton',
            'provides': 'examples.resources.src.sum_wrapper.SumWrapper',
            'kwargs_factory': {
                'sh': {
                    'handler': {'container': 'sum_handler'}
                },
                'sh_s': {
                    'handler': {'container': 'sum_handler_s'}
                },
            }
        },
    }
)

a = 2
b = 3
print(f"sum_wrapper__sh: {container.sum_wrapper__sh().sum(a, b)}")
print(f"sum_wrapper__sh_s: {container.sum_wrapper__sh_s().sum(a, b)}")
print(f"sum_wrapper_s__sh: {container.sum_wrapper_s__sh().sum(a, b)}")
print(f"sum_wrapper_s__sh_s: {container.sum_wrapper_s__sh_s().sum(a, b)}")

print(f"sum_wrapper__sh === sum_wrapper__sh ? {container.sum_wrapper__sh() is container.sum_wrapper__sh()}")
print(f"sum_wrapper__sh === sum_wrapper__sh_s ? {container.sum_wrapper__sh() is container.sum_wrapper__sh_s()}")
print(f"sum_wrapper__sh === sum_wrapper_s__sh ? {container.sum_wrapper__sh() is container.sum_wrapper_s__sh()}")
print(f"sum_wrapper__sh === sum_wrapper_s__sh_s ? {container.sum_wrapper__sh() is container.sum_wrapper_s__sh_s()}")
print(f"sum_wrapper__sh_s === sum_wrapper__sh_s ? {container.sum_wrapper__sh_s() is container.sum_wrapper__sh_s()}")
print(f"sum_wrapper__sh_s === sum_wrapper_s__sh ? {container.sum_wrapper__sh_s() is container.sum_wrapper_s__sh()}")
print(f"sum_wrapper__sh_s === sum_wrapper_s__sh_s ? {container.sum_wrapper__sh_s() is container.sum_wrapper_s__sh_s()}")
print(f"sum_wrapper_s__sh === sum_wrapper_s__sh ? {container.sum_wrapper_s__sh() is container.sum_wrapper_s__sh()}")
print(f"sum_wrapper_s__sh === sum_wrapper_s__sh_s ? {container.sum_wrapper_s__sh() is container.sum_wrapper_s__sh_s()}")
print(f"sum_wrapper_s__sh_s === sum_wrapper_s__sh_s ? {container.sum_wrapper_s__sh_s() is container.sum_wrapper_s__sh_s()}")