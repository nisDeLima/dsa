class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr, numbers):
            numbers.append(str(curr.val))
            if not curr.left and not curr.right:
                self.res += int("".join(numbers), 2)
                numbers.pop()
                return
            if curr.left:
                dfs(curr.left, numbers)
            if curr.right:
                dfs(curr.right, numbers)
            numbers.pop()
        
        dfs(root, [])
        return self.res
