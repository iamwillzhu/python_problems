from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

@dataclass
class BinaryTreeNode:
    data: int = 0
    left: Optional[BinaryTreeNode] = None
    right: Optional[BinaryTreeNode] = None
