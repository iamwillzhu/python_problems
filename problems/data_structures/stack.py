from dataclasses import dataclass
from typing import Optional

from problems.data_structures.list_node import ListNode

@dataclass
class Stack:
    top: Optional[ListNode] = None

    def peek(self) -> int:
        if self.top is None:
            raise Exception("The stack is empty")
        return self.top.data

    def pop(self) -> int:
        if self.top is None:
            raise Exception("The stack is empty")
        temp = self.top
        self.top = temp.next
        return temp.data

    def push(self, data: int) -> None:
        new_node = ListNode(data)
        new_node.next = self.top
        self.top = new_node

    def empty(self) -> bool:
        return self.top is None
