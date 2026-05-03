class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        @cache
        def backtrack(i, current_sum):
            if i == len(stones):
                return abs(total - 2 * current_sum)

            if current_sum > target:
                return abs(total - 2 * current_sum)

            include = backtrack(i + 1, current_sum + stones[i])
            exclude = backtrack(i + 1, current_sum)

            return min(include, exclude)

        return backtrack(0, 0)
