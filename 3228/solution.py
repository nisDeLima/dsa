class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ops = 0
        in_zero_block = False

        for c in s:
            if c == "1":
                ones += 1
                in_zero_block = False
            else:
                if not in_zero_block:
                    ops += ones
                    in_zero_block = True

        return ops

