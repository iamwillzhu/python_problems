from problems.data_structures.list_node import ListNode
from typing import Optional

def merge_sorted_linked_lists(list_one: Optional[ListNode], list_two: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head: ListNode = ListNode()
    tail: ListNode = dummy_head 

    while list_one is not None and list_two is not None:
        if list_one.data < list_two.data: 
            tail.next = list_one
            list_one = list_one.next
        else:
            tail.next = list_two
            list_two = list_two.next

        tail = tail.next
    tail.next = list_one or list_two

    return dummy_head.next
