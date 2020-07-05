from typing import List
from dataclasses import dataclass

class MaxWithCount:
    def __init__(self, max: int) -> None:
        self.max: int = max
        self.count: int = 1

class MaxStack:
    def __init__(self) -> None:
        self._element: List[int] = []
        self._cached_max_with_count: List[MaxWithCount] = []

    def empty(self) -> bool:
        return len(self._element) == 0

    def max(self) -> int:
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._cached_max_with_count[-1].max

    def pop(self) -> int:
        if self.empty():
            raise IndexError('pop(): empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max
        if pop_element == current_max:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return pop_element

    def push(self, value: int) -> None:
        self._element.append(value)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(MaxWithCount(max=value))
        else:
            current_max = self._cached_max_with_count[-1].max
            if value == current_max:
                self._cached_max_with_count[-1].count += 1
            elif value > current_max:
                self._cached_max_with_count.append(MaxWithCount(max=value))

