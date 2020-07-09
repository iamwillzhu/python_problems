from problems.arrays.spiral_matrix import matrix_in_spiral_order

class TestMatrixInSpiralOrder:
    def test_square_matrix_odd(self):
        square_matrix = [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]
        square_matrix_spiral_order = [
                1,2,3,6,9,8,7,4,5]

        assert(matrix_in_spiral_order(
            square_matrix) == square_matrix_spiral_order)

    def test_square_matrix_even(self):
        square_matrix = [
                [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]
            ]
        square_matrix_spiral_order = [
                1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

        assert(matrix_in_spiral_order(
            square_matrix) == square_matrix_spiral_order)
