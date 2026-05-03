class Solution:
    def calc_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.calc_height(root.left), self.calc_height(root.right)) + 1

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.calc_height(root)
        width = (2 ** height) - 1
        grid = [[""] * width for _ in range(height)]

        queue = deque([(root, 0, (width - 1) // 2)])

        while queue:
            node, row, col = queue.popleft()
            grid[row][col] = str(node.val)

            offset = 2 ** (height - row - 2)
            if node.left:
                queue.append((node.left, row + 1, col - offset))
            if node.right:
                queue.append((node.right, row + 1, col + offset))

        return grid
