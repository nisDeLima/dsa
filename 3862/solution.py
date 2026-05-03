class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + num
        
        suffix_prod = 1
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                suffix_prod *= nums[i + 1]
            if prefix_sum[i] == suffix_prod:
                return i
        
        return -1
