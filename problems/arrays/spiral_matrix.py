from typing import List

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    spiral_ordering: List[int] = []

    def matrix_layer_in_clockwise(offset: int) -> None:
        if offset == len(square_matrix) - offset - 1:
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset:-1-offset])
        spiral_ordering.extend(
                list(zip(*square_matrix))[-1-offset][offset:-1-offset])
        spiral_ordering.extend(
                square_matrix[-1-offset][-1-offset:offset:-1])
        spiral_ordering.extend(
                list(zip(*square_matrix))[offset][-1-offset:offset:-1])

    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)
    return spiral_ordering
