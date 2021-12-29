# Definition for a Node.
from typing import Optional
from collections import dedq

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return 
        if root.left:
            left, right = root.left, root.left
            self.connect(left)
            self.connect(right)
            while left:
                left.next = right
                left, right = left.right, right.left
        return root
            
                