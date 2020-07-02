from __future__ import annotations
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class ListNode:
    data: int = 0
    next: Optional[ListNode] = None

    def __str__(self):
        current_node: Optional[ListNode] = self
        values: List[str] = [str(current_node.data)]
        
        current_node = current_node.next
        while current_node is not None:
            values.append(str(current_node.data))
            current_node = current_node.next

        return "->".join(values)

    @classmethod
    def from_list(cls, values: List[int]) -> Optional[ListNode]:
        dummy_head: ListNode = cls()
        tail: ListNode = dummy_head

        for value in values:
            tail.next = cls(data=value)
            tail = tail.next

        return dummy_head.next
