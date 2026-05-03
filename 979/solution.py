# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(curr):
            if not curr:
                return 0
            extra_coins = (curr.val - 1) + dfs(curr.left) + dfs(curr.right)
            self.res += abs(extra_coins)
            return extra_coins
        dfs(root)
        return self.res
