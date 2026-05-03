# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(head):
            prev, curr = None, head

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev

        tail = reverse_list(head)
        dummy = ListNode(val=float("-inf"), next=tail)
        curr, prev = tail, dummy

        while curr:
            if prev.val <= curr.val:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next

        return reverse_list(dummy.next)
