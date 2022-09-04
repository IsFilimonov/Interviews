from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right
        
    
def search(n: int, root: Optional[Node]) -> bool:
    if not root:
        return False
    if root.value == n:
        return True
    return search(n, root.left) or search(n, root.right)