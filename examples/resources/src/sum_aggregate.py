from examples.resources.src.sum_object import SumObject

class SumAggregate:
    def __init__(self, sum_object: SumObject) -> None:
        self.sum_object = sum_object

    def sum(self) -> int:
        return self.sum_object.sum()