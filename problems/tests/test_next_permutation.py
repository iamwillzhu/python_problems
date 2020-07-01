from problems.array.next_permutation import next_permutation

class TestNextPermutation:
    def test_no_next_permutation(self) -> None:
        perm = [4,3,2,1]
        expected_result = []

        assert(next_permutation(perm) == expected_result)

    def test_next_permutation_one(self) -> None:
        perm = [1,2,3,4]
        expected_result = [1,2,4,3]

        assert(next_permutation(perm) == expected_result)

    def test_next_permutation_two(self) -> None:
        perm = [1,4,3,2]
        expected_result = [2,1,3,4]

        assert(next_permutation(perm) == expected_result)
