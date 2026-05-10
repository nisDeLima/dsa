class Solution_rmvd:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        def can_jump(i, j):
            return i < j and (-target <= nums[j] - nums[i] <= target)
        
        adj = [[] for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if can_jump(i, j):
                    adj[i].append(j)
        
        @cache
        def get_max(curr):
            if curr == len(nums) - 1:
                return 0
            
            jumps = float("-inf")
            for nei in adj[curr]:
                test_nei = get_max(nei) + 1
                jumps = max(jumps, test_nei)

            return jumps

        max_jumps = get_max(0)

        return max_jumps if max_jumps != float("-inf") else -1



class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == -1:
                continue
            
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[n - 1]
