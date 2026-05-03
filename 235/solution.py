# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_side = min(p.val, q.val)
        max_side = max(p.val, q.val)

        if min_side <= root.val <= max_side:
            return root
        elif root.val < min_side:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > max_side:
            return self.lowestCommonAncestor(root.left, p, q)
