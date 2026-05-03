"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root])

        while queue:
            prev = None
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    curr.next = None
                    if prev:
                        prev.next = curr
                    prev = curr
                    if curr.right and curr.left:
                        queue.append(curr.left) 
                        queue.append(curr.right) 
                        
        return root
