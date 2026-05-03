class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        self.k = k

        def _reverse(l, r):
            count = 0
            curr = l
            prev = r.next
            while count < self.k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                count += 1

        left = right = head
        new_head = head
        last_tail = None
        while right:
            for _ in range(k - 1):
                right = right.next
                if not right:
                    break
            if not right:
                break
            _reverse(left, right)

            if new_head == head:
                new_head = right
            if last_tail is not None:
                last_tail.next = right
            last_tail = left

            left = right = left.next

        return new_head
