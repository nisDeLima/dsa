class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = nums[0]
        res = 0

        for i in range(1, len(nums)):
            if nums[i] <= prev:
                res += prev - nums[i] + 1
                prev = nums[i] + (prev - nums[i] + 1)
            else:
                prev = nums[i]
        
        return res
