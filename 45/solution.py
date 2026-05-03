class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(i):
            if cache[i] != -1:
                return cache[i]

            if i == len(nums) - 1:
                cache[i] = 0
                return cache[i]

            min_jumps = float("inf")

            for jump in range(1, nums[i] + 1):
                if i + jump <= len(nums) - 1:
                    min_jumps = min(min_jumps, dfs(i + jump) + 1)
            cache[i] = min_jumps
            return cache[i]
        return dfs(0)

