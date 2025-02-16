from examples.resources.src.sum_handler import SumHandler

class SumWrapper(object):
    def __init__(self, handler: SumHandler) -> None:
        self.handler = handler

    def sum(self, a: int, b: int) -> int:
        return self.handler.sum(a, b)