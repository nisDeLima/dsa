class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(0), ListNode(0)
        left_tail, right_tail = left, right
        curr = head

        while curr:
            if curr.val < x:
                left_tail.next = curr
                left_tail = left_tail.next
            else:
                right_tail.next = curr
                right_tail = right_tail.next
            curr = curr.next

        right_tail.next = None
        left_tail.next = right.next

        return left.next

