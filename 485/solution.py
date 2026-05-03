class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0

        for num in nums:
            if num == 0:
                curr = 0
            curr += num
            res = max(res, curr)
        
        return res
