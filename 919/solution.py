class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.deque = deque()
        
        # Pre-process: BFS to find all nodes, keep incomplete ones
        queue = deque([root])
        while queue:
            node = queue.popleft()
            # Only keep nodes that could be future parents
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def insert(self, val: int) -> int:
        # The front of deque is ALWAYS the next parent
        parent = self.deque[0]
        node = TreeNode(val)
        
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            # Parent is now complete, remove it
            self.deque.popleft()
        
        # New node could be a future parent
        self.deque.append(node)
        return parent.val
    
    def get_root(self) -> Optional[TreeNode]:
        return self.root
