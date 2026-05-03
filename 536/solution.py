class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s: 
            return None
        
        i = 0
        if s[0] == '-':
            i = 1
        while i < len(s) and s[i].isdigit():
            i += 1
        
        root = TreeNode(int(s[:i]))
        stack = [root]
        
        while i < len(s):
            if s[i] == '(':
                # Next number is coming, prepare to parse
                i += 1
                # Find the number
                start = i
                if i < len(s) and s[i] == '-':
                    i += 1
                while i < len(s) and s[i].isdigit():
                    i += 1
                
                node = TreeNode(int(s[start:i]))
                
                # Attach to parent: left first, then right
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
                
                stack.append(node)
                
            elif s[i] == ')':
                # Done with this subtree
                stack.pop()
                i += 1
            else:
                i += 1
        
        return root
