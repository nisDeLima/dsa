class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        LEN = len(s)

        def backtrack(i, curr):
            if i >= LEN:
                res.append(curr[:])
                return

            for j in range(i, LEN):
                if self.isPalin(s, i, j):
                    curr.append(s[i:j + 1])
                    backtrack(j + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return res

    def isPalin(self, s, l, r):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
