from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        curr = sum(i * num for i, num in enumerate(nums))
        res = curr

        for k in range(1, n):
            curr = curr + total - n * nums[-k]
            res = max(res, curr)

        return res
