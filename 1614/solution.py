class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        count = 0

        for char in s:
            if char == "(":
                count += 1
                res = max(res, count)
            if char == ")":
                count -= 1
        return res
