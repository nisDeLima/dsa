"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten_rmvd(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def get_tail(curr):
            while curr:
                prev = curr
                curr = curr.next

            return prev
        dummy = Node(0, None, head)

        curr = dummy.next

        while curr:
            if curr.child:
                child_tail = get_tail(curr.child)
                child_tail.next = curr.next
                if curr.next:
                    curr.next.prev = child_tail
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            curr = curr.next
        
        return dummy.next

    def flatten_rmvd(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        curr = head

        def add_to_stack(node):
            if node:
                stack.append(node) 
                add_to_stack(node.child)
                add_to_stack(node.next)
        
        add_to_stack(head)

        for i in range(len(stack)):
            stack[i].child = None
            if i > 0:
                stack[i].prev = stack[i - 1]
            if i < len(stack) - 1:
                stack[i].next = stack[i + 1]

        return head
    def flatten_rmvd2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        curr = head

        def add_to_stack(node):
            if node:
                stack.append(node) 
                add_to_stack(node.child)
                add_to_stack(node.next)
        
        add_to_stack(head)

        for i in range(len(stack)):
            stack[i].child = None
            if i > 0:
                stack[i].prev = stack[i - 1]
            if i < len(stack) - 1:
                stack[i].next = stack[i + 1]

        return head
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        def flatten(node):
            curr = node
            last = None

            while curr:
                next_node = curr.next

                if curr.child:
                    # *burp* Recursively flatten the child
                    child_tail = flatten(curr.child)

                    # Insert flattened child between curr and next
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None

                    # Connect the tail of child list to next_node
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail

                    last = child_tail
                else:
                    last = curr

                curr = next_node

            return last  # Return the tail of this level

        flatten(head)
        return head 
