class Solution_rmv:
    def longestSquareStreak(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        dp = [1] * N

        for i in range(len(nums) - 1, - 1, - 1):
            for j in range(i + 1, len(nums)):
                cand = float("-inf")
                if (nums[i] * nums[i]) == nums[j]:
                    cand = dp[j] + 1
                dp[i] = max(dp[i], cand)
        
        max_dp = max(dp) 

        return max_dp if max_dp >= 2 else -1
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)
        visited = set()
        nums.sort()
        best = -1

        for num in nums:
            if num in visited:
                continue
                
            length = 1
            curr = num
            while curr * curr in num_set:
                curr = curr * curr
                visited.add(curr)
                length += 1
            if length >= 2:
                best = max(best, length)

        return best
