class Solution:
    def minFlips(self, s: str) -> int:
        L = len(s)
        ss = s + s

        p1 = 0  # mismatches vs "010101..."
        p2 = 0  # mismatches vs "101010..."

        # build initial window [0..L-1]
        for i in range(L):
            if i % 2 == 0:
                if ss[i] == "1": p1 += 1
                else: p2 += 1
            else:
                if ss[i] == "1": p2 += 1
                else: p1 += 1

        result = min(p1, p2)

        # slide window
        l = 0
        for r in range(L, 2*L):
            # remove leftmost character
            if ss[l] != ("0" if l % 2 == 0 else "1"): p1 -= 1
            if ss[l] != ("1" if l % 2 == 0 else "0"): p2 -= 1

            # add new right character
            if ss[r] != ("0" if r % 2 == 0 else "1"): p1 += 1
            if ss[r] != ("1" if r % 2 == 0 else "0"): p2 += 1

            l += 1
            result = min(result, p1, p2)

        return result
