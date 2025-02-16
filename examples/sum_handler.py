from examples.resources.src.container_test_init import container_init

container = container_init({
    'sum_handler': {
        'provider': 'Factory',
        'provides': 'examples.resources.src.sum_handler.SumHandler',
    },
    'sum_handler_s': {
        'provider': 'Singleton',
        'provides': 'examples.resources.src.sum_handler.SumHandler',
    }
})

a = 1
b = 1
print(f"sum_handler: {container.sum_handler().sum(a, b)}")
print(f"sum_handler_s: {container.sum_handler_s().sum(a, b)}")

print(f"sum_handler === sum_handler ? {container.sum_handler() is container.sum_handler()}")
print(f"sum_handler === sum_handler_s ? {container.sum_handler() is container.sum_handler_s()}")
print(f"sum_handler_s === sum_handler_s ? {container.sum_handler_s() is container.sum_handler_s()}")