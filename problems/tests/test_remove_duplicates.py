from problems.data_structures.list_node import ListNode
from problems.linked_list.remove_duplicates import remove_duplicates

class TestRemoveDuplicates:
    def test_remove_duplicates(self) -> None:
        linked_list = ListNode.from_list([2,2,4,5,6,9,10,10,10])
        expected_result = ListNode.from_list([2,4,5,6,9,10])

        assert(remove_duplicates(head=linked_list) == expected_result)

    def test_no_duplicates(self) -> None:
        linked_list = ListNode.from_list([2,4,5,6,9,10])
        assert(remove_duplicates(head=linked_list) == linked_list)
