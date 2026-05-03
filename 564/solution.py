class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        L = len(n)
        candidates = set()

        # ── Edge cases ────────────────────────────────────────────────────────
        # If the answer has FEWER digits than n: largest such palindrome is 999...9
        # e.g. n is 4 digits → 999
        candidates.add(10 ** (L - 1) - 1)

        # If the answer has MORE digits than n: smallest such palindrome is 100...01
        # e.g. n is 4 digits → 10001
        candidates.add(10 ** L + 1)

        # ── Mirror candidates ─────────────────────────────────────────────────
        # The nearest palindrome almost always comes from mirroring the first half.
        # We try prefix-1, prefix, prefix+1 to cover cases where mirroring
        # the first half as-is overshoots or undershoots.
        #
        #   n = 1 2 3 4 5
        #       ↑ ↑ ↑            ← first half (ceil) = "123"
        #             ↑ ↑        ← replaced by mirroring: "12321"

        half_len = (L + 1) // 2
        prefix = int(n[:half_len])

        for delta in (-1, 0, 1):
            p = str(prefix + delta)

            # Even length: "12" → "1221"
            # Odd  length: "123" → "12321" (middle char not mirrored)
            if L % 2 == 0:
                palindrome = int(p + p[::-1])
            else:
                palindrome = int(p + p[-2::-1])

            candidates.add(palindrome)

        # ── Pick the winner ───────────────────────────────────────────────────
        # Remove n itself — problem says it can't be the answer.
        # Then pick closest. Tie-break: smaller number wins.
        candidates.discard(num)
        return str(min(candidates, key=lambda x: (abs(x - num), x)))
