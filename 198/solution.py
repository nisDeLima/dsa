class Solution:
    def rob_remove(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def get_max(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            take = nums[i] + get_max(i + 2)
            skip = get_max(i + 1)

            cache[i] = max(take, skip)
            return cache[i]
        return get_max(0)
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        dp = [nums[0], max(nums[0], nums[1])]

        for num in nums[2:]:
            curr_max = max(num + dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = curr_max
        
        return dp[1]
