# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: 
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = ListNode() 
        last_odd = odds
        evens = ListNode() 
        last_even = evens

        is_odd = True

        curr = head

        while curr:
            if is_odd:
                last_odd.next = curr
                last_odd = last_odd.next
            else:
                last_even.next = curr
                last_even = last_even.next
            is_odd = not is_odd
            curr = curr.next

        if evens.next != None:
            last_odd.next = evens.next
            last_even.next = None
        
        return odds.next
