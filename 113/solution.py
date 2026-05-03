# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def dfs(curr, curr_sum, curr_arr):
            if not curr:
                return
            curr_sum += curr.val
            curr_arr.append(curr.val)
            # Check leaf
            if not curr.right and not curr.left:
                if curr_sum == targetSum:
                    self.res.append(curr_arr.copy())
            else:
                dfs(curr.left, curr_sum, curr_arr)
                dfs(curr.right, curr_sum, curr_arr)
            curr_sum -= curr.val
            curr_arr.pop()
            return
        dfs(root, 0, [])
        return self.res
