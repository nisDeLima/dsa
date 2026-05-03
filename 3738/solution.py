class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prefix = [1] * len(nums)
        sufix = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                prefix[i] += prefix[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                sufix[i] += sufix[i + 1]
        
        ans = max(prefix)


        for i in range(len(nums)):
            if 0 < i < len(nums) - 1 and nums[i - 1] <= nums[i + 1]: 
                ans = max(ans, prefix[i - 1] + 1 + sufix[i + 1])
            if i > 0:
                ans = max(ans, prefix[i - 1] + 1)
            if i < len(nums) - 1:
                ans = max(ans, sufix[i + 1] + 1)
        return ans
