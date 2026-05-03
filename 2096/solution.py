# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections_work_but_slow(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.start_node = None

        def setup_tree(curr, par):
            if not curr:
                return
            if curr.val == startValue:
                self.start_node = curr
            if par != -1:
                curr.up = par
            else:
                curr.up = None
            
            setup_tree(curr.left, curr)
            setup_tree(curr.right, curr)
            
        setup_tree(root, -1)

        queue = deque([(self.start_node, "")])  # node, directions took so far
        seen = set()
        
        while queue:
            curr, directions = queue.popleft()
            
            if curr.val == destValue:
                return directions
            
            if curr in seen:
                continue
                
            seen.add(curr)
            
            if curr.left:
                queue.append((curr.left, directions + "L"))
            if curr.right:
                queue.append((curr.right, directions + "R"))
            if curr.up:
                queue.append((curr.up, directions + "U"))
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # Find path from root to start and dest
        def find_path(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            
            # Try left
            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()
            
            # Try right
            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()
            
            return False
        
        start_path = []
        dest_path = []
        
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)
        
        # Remove common prefix (that's your LCA path)
        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1
        
        # Everything left in start_path needs to go UP
        # Everything left in dest_path is the path down to dest
        return "U" * (len(start_path) - i) + "".join(dest_path[i:])
