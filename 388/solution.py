class Solution:
    def rotatedDigits(self, n: int) -> int:
        digits = list(map(int, str(n)))

        same = {0, 1, 8}
        change = {2, 5, 6, 9}

        @cache
        def dp(pos, tight, has_change):
            if pos == len(digits):
                return 1 if has_change else 0

            limit = digits[pos] if tight else 9
            res = 0

            for d in range(limit + 1):
                if d not in same and d not in change:
                    continue

                new_tight = tight and (d == limit)
                new_has_change = has_change or (d in change)

                res += dp(pos + 1, new_tight, new_has_change)

            return res

        return dp(0, True, False)
