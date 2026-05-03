# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: 
                return (0, 0)

            left = dfs(root.left)
            right = dfs(root.right)

            rob_current = root.val + left[1] + right[1]
            skip_current = max(left) + max(right)

            return (rob_current, skip_current)

        return max(dfs(root))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(root):
            if not root:
                return 0

            rob = root.val
            not_rob = dfs(root.left) + dfs(root.right)

            if root.left:
                rob += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                rob += dfs(root.right.left) + dfs(root.right.right)

            return max(rob, not_rob)
        return dfs(root)
