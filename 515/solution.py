# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []

        while queue:
            curr_res = float("-inf")
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    curr_res = max(curr.val, curr_res)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if curr_res != float("-inf"):
                res.append(curr_res)
        
        return res
