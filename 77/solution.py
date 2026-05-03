class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        curr = []

        def backtrack(start):
            if len(curr) == k:
                ans.append(curr.copy())
                return

            for num in range(start, n + 1):
                curr.append(num)
                backtrack(num + 1)
                curr.pop()

        backtrack(1)
        return ans

