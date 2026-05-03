# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.ans = None
        self.deepest = 0 

        def dfs(curr, lvl):
            if not curr:
                return lvl

            left_lvl = dfs(curr.left, lvl + 1)
            right_lvl = dfs(curr.right, lvl + 1)
            depth = max(right_lvl, left_lvl)

            self.deepest = max(self.deepest, depth)

            if left_lvl == right_lvl and left_lvl == self.deepest:
                self.ans = curr

            return depth
        
        dfs(root, 0)
        return self.ans
