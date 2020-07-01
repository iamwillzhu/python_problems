from typing import List
def next_permutation(perm: List[int]) -> List[int]:
    inversion_pivot: int = len(perm) - 2

    while (inversion_pivot >= 0 and 
            perm[inversion_pivot] >= perm[inversion_pivot + 1]):
        inversion_pivot -= 1

    if inversion_pivot == -1:
        return []

    for smallest_greater_idx in reversed(range(inversion_pivot + 1, len(perm))):
        if perm[smallest_greater_idx] > perm[inversion_pivot]:
            perm[smallest_greater_idx], perm[inversion_pivot] = \
                    perm[inversion_pivot], perm[smallest_greater_idx]
            break

    perm[inversion_pivot + 1:] = reversed(perm[inversion_pivot + 1:])
    return perm
