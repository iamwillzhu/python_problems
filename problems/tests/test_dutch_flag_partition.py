from problems.arrays.dutch_flag_partition import dutch_flag_partition
from typing import List

import pytest

def all_equal_to(subarray: List[int], start: int, end: int, pivot: int) -> bool:
    for val in subarray[start:end]:
        if val != pivot:
            return False
    return True

def all_greater_than(subarray: List[int], start: int, pivot: int) -> bool:
    for val in subarray[start:]:
        if val <= pivot:
            return False
    return True

class TestDutchFlagPartition:
    def test_simple_flag_one(self) -> None:
        pivot_index: int = 0
        A: List[int] = [1,2,0,0,2,1,2,1]
        expected_result = [0,0,1,1,1,2,2,2]

        dutch_flag_partition(pivot_index, A)
        assert(A == expected_result)

    def test_simple_flag_two(self) -> None:
        pivot_index: int = 2
        A: List[int] = [1,2,0,0,2,1,2,1]

        dutch_flag_partition(pivot_index, A)
        assert(all_equal_to(subarray=A, start=0, end=2, pivot=0) and
                all_greater_than(subarray=A, start=2, pivot=0))
        
