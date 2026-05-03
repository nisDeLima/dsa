# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        sort_list = [] # col, row, val

        def populate(curr, row, col):
            if curr:
                sort_list.append((col, row, curr.val))
                populate(curr.left, row + 1, col - 1)
                populate(curr.right, row + 1, col + 1)

        populate(root, 0, 0)
        sort_list.sort()

        res = []
        curr_list = []
        prev_col = None

        for col, row, val in sort_list:
            if not curr_list or col == prev_col:
                curr_list.append(val)
                prev_col = col
            else:
                res.append(curr_list.copy())
                prev_col = col
                curr_list = []
                curr_list.append(val)
        res.append(curr_list.copy()) 
        return res

