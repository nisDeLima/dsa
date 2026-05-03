class Codec:

    def serialize_(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        serialization = []

        def dfs(curr):
            if not curr:
                return
            serialization.append(str(curr.val))
            dfs(curr.left)
            dfs(curr.right)

        dfs(root)

        return "-".join(serialization)

    def deserialize_(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return []
        binary_elements = data.split("-")
        binary_integers = [int(elm) for elm in binary_elements]
        root = TreeNode(binary_integers[0])

        def add(curr, elm):
            if not curr:
                return TreeNode(elm)
            if curr.val > elm:
                curr.left = add(curr.left, elm)
            elif curr.val < elm:
                curr.right = add(curr.right, elm)
            return curr
        for elm in binary_integers[1:]:
            add(root, elm)
        
        return root

    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return " ".join(vals)

    def deserialize(self, data):
        if not data:
            return None

        vals = list(map(int, data.split()))
        i = 0

        def build(low, high):
            nonlocal i
            if i == len(vals):
                return None

            v = vals[i]
            if not (low < v < high):
                return None

            i += 1
            node = TreeNode(v)
            node.left = build(low, v)
            node.right = build(v, high)
            return node

        return build(float("-inf"), float("inf"))

