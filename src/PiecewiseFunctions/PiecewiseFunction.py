from abc import ABC, abstractmethod
from typing import Tuple


class PiecewiseFunction(ABC):
    @abstractmethod
    def evaluate(self, x: float) -> float:
        pass

    @abstractmethod
    def minimum(self) -> Tuple[float, float]:
        pass

    @abstractmethod
    def maximum(self) -> Tuple[float, float]:
        pass
