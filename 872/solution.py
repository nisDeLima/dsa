# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False

        leaves_one = []
        leaves_two = []


        def config_leaves(curr, storage):
            if not curr:
                return
            if not curr.left and not curr.right:
                storage.append(curr.val)
            
            config_leaves(curr.left, storage)
            config_leaves(curr.right, storage)
        
        config_leaves(root1, leaves_one)
        config_leaves(root2, leaves_two)

        return leaves_one == leaves_two
