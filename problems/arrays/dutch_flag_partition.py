from typing import List
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot: int = A[pivot_index]

    smaller: int = 0
    equal: int = 0
    larger: int = len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1

        elif A[equal] == pivot:
            equal += 1

        elif A[equal] > pivot:
            larger -=1
            A[equal], A[larger] = A[larger], A[equal]
