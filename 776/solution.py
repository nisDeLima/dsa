# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        def dfs(curr):
            if not curr:
                return [None, None]
            if curr.val > target:
                equal_less, greater = dfs(curr.left)
                curr.left = greater
                return [equal_less, curr]
            else:
                equal_less, greater = dfs(curr.right)
                curr.right = equal_less
                return [curr, greater]
        return dfs(root)
                
