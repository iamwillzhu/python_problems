from problems.data_structures.list_node import ListNode
from problems.linked_lists.merge_sorted_linked_lists import merge_sorted_linked_lists

# TODO: this function isn't really used anywhere but could be helpful somewhere in the future
def is_linked_list_sorted(linked_list) -> bool:
    if linked_list is None:
        return True

    past_value = linked_list.data
    current_node = linked_list.next
    while current_node is not None:
        if current_node.data < past_value:
            return False
        else:
            past_value = current_node.data
            current_node = current_node.next

    return True


class TestMergeSortedLinkedLists:
    def test_merge_sorted_linked_lists(self) -> None:
        list_one = ListNode.from_list(values=[4,10])
        list_two = ListNode.from_list(values=[3,7,9])

        merged_list = merge_sorted_linked_lists(list_one, list_two)
        assert(merged_list == ListNode.from_list([3,4,7,9,10]))

    def test_only_list_one_not_none(self) -> None:
        list_one = ListNode.from_list(values=[4,10])
        list_two = None

        merged_list = merge_sorted_linked_lists(list_one, list_two)
        assert(merged_list == list_one)
    
    def test_only_list_two_not_none(self) -> None:
        list_one = None 
        list_two = ListNode.from_list(values=[3,7,9])

        merged_list = merge_sorted_linked_lists(list_one, list_two)
        assert(merged_list == list_two)
