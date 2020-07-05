from problems.data_structures.list_node import ListNode
from typing import Optional

def remove_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current_node: Optional[ListNode] = head
    next_node: Optional[ListNode]

    while current_node is not None:
        next_node = current_node.next

        while next_node is not None and next_node.data == current_node.data:
            next_node = next_node.next

        current_node.next = next_node
        current_node = current_node.next

    return head
