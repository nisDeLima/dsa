class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr = 0
        res = 0
        for num in nums:
            if num == 0:
                curr += 1
                res += curr
            else:
                curr = 0

        return res

