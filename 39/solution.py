class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if sum(curr) > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            dfs(i, curr)
            curr.pop()
            dfs(i + 1, curr)
        dfs(0, [])

        return res
