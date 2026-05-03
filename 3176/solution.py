class Solution:
    # I'm stupid and did for subarrays :p
    def maximumLength_removed(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        tagged = set()
        res = 1
        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                tagged.add(r - 1)
            while len(tagged) > k:
                tagged.discard(l)
                l += 1
            res = max(res, r - l + 1)

        return res
    def maximumLength_memory_exceeded(self, nums: List[int], k: int) -> int:
        @cache
        def dp(i: int, prev: int, violations: int) -> int:
            if i >= len(nums):
                return 0

            # Skip current element
            skip = dp(i + 1, prev, violations)

            # Take current element
            take = 0
            if prev == -1:  # First element
                take = 1 + dp(i + 1, nums[i], violations)
            elif nums[i] == prev:  # No new violation
                take = 1 + dp(i + 1, nums[i], violations)
            elif violations < k:  # Can afford a violation
                take = 1 + dp(i + 1, nums[i], violations + 1)

            return max(skip, take)
    
        return dp(0, -1, 0)       

    def maximumLength_just_wrong(self, nums: List[int], k: int) -> int:
        @cache
        def get_max(i, violations):
            if i >= len(nums):
                return 0, 0  # (length, violations_used)

            # Skip this element
            skip_len, skip_viols = get_max(i + 1, violations)

            # Take this element - need to check all future elements
            best_take_len = 1
            best_take_viols = violations

            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    # No new violation
                    future_len, future_viols = get_max(j, violations)
                else:
                    # Costs a violation
                    future_len, future_viols = get_max(j, violations + 1)

                if future_viols <= k:
                    if future_len + 1 > best_take_len:
                        best_take_len = future_len + 1
                        best_take_viols = future_viols

            # Compare skip vs take
            if best_take_viols <= k and skip_viols <= k:
                if best_take_len >= skip_len:
                    return best_take_len, best_take_viols
                else:
                    return skip_len, skip_viols
            elif best_take_viols <= k:
                return best_take_len, best_take_viols
            else:
                return skip_len, skip_viols

        result, _ = get_max(0, 0)
        return result
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i][v] = max length of subsequence ending at i with v violations
        dp = [[0] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = 1  # Single element, no violations
        
        for i in range(1, n):
            for j in range(i):
                for v in range(k + 1):
                    if nums[i] == nums[j]:
                        # No new violation
                        dp[i][v] = max(dp[i][v], dp[j][v] + 1)
                    elif v > 0:
                        # Use one violation
                        dp[i][v] = max(dp[i][v], dp[j][v - 1] + 1)
        
        return max(max(row) for row in dp)
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        @cache
        def rec(i, violations):
            best = 1

            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    best = max(best, rec(j, violations) + 1)
                elif violations < k:
                    best = max(best, rec(j, violations + 1) + 1)
            return best

        res = 0
        for i in range(len(nums)):
            res = max(res, rec(i, 0))
        
        return res
