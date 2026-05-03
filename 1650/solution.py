"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor_rmvd(self, p: 'Node', q: 'Node') -> 'Node':
        self.res = None
        
        # Find root by following parent pointers like a normal person
        def find_root(node):
            while node.parent:
                node = node.parent
            return node
        
        def dfs(curr):
            if not curr:
                return False, False # no p, no q
            
            right_explore = dfs(curr.right)
            left_explore = dfs(curr.left)

            is_there_p = curr == p or right_explore[0] or left_explore[0]
            is_there_q = curr == q or right_explore[1] or left_explore[1]

            if self.res == None and (is_there_p and is_there_q):
                self.res = curr
            
            return is_there_p, is_there_q
        
        root = find_root(p)  # or find_root(q), doesn't matter, same tree genius
        dfs(root)
        return self.res

    def lowestCommonAncestor_rmvd2(self, p: 'Node', q: 'Node') -> 'Node':
        p_parents = set()

        curr = p
        while curr:
            p_parents.add(curr)
            curr = curr.parent

        curr = q
        while curr:
            if curr in p_parents:
                return curr
            curr = curr.parent
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Two pointers starting at p and q
        pointer1, pointer2 = p, q
        
        # Keep walking up until they meet
        # When a pointer hits root (None), redirect it to the OTHER starting node
        # This ensures both pointers travel the same total distance
        while pointer1 != pointer2:
            # Move pointer1 up, or switch to q's path if we hit the top
            pointer1 = pointer1.parent if pointer1 else q
            
            # Move pointer2 up, or switch to p's path if we hit the top
            pointer2 = pointer2.parent if pointer2 else p
        
        # Both pointers now point to the LCA
        return pointer1
