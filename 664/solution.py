class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Optional optimization: compress consecutive duplicates,
        # since "aaa" is same as "a" for printing turns.
        compressed = []
        for ch in s:
            if not compressed or compressed[-1] != ch:
                compressed.append(ch)
        s = "".join(compressed)
        n = len(s)

        @lru_cache(None)
        def dp(l: int, r: int) -> int:
            if l > r:
                return 0
            if l == r:
                return 1

            # Baseline: print s[l] alone, then the rest.
            res = 1 + dp(l + 1, r)

            # Try to merge s[l] with a same character at position k.
            for k in range(l + 1, r + 1):
                if s[k] == s[l]:
                    # We can "share" the print for s[l] and s[k]
                    # so we don't pay the +1 separately.
                    res = min(res, dp(l + 1, k - 1) + dp(k, r))

            return res

        return dp(0, n - 1)

