from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        tree_arr = deque()

        i = 0
        n = len(traversal)

        # your populate_arr idea, just not wrong
        while i < n:
            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1

            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1

            tree_arr.append((val, depth))

        root = TreeNode(tree_arr.popleft()[0])

        def create_tree(curr, lvl):
            if not tree_arr or tree_arr[0][1] <= lvl:
                return

            if tree_arr and tree_arr[0][1] == lvl + 1:
                curr.left = TreeNode(tree_arr.popleft()[0])
                create_tree(curr.left, lvl + 1)

            if tree_arr and tree_arr[0][1] == lvl + 1:
                curr.right = TreeNode(tree_arr.popleft()[0])
                create_tree(curr.right, lvl + 1)

        create_tree(root, 0)
        return root

