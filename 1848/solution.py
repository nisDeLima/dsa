class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        candidates = []
        for idx, num in enumerate(nums):
            if num == target:
                candidates.append(idx)

        res = abs(candidates[0] - start)

        for cand in candidates:
            res = min(res, abs(cand - start))
        
        return res
