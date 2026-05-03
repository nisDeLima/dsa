class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        res = float("inf")
        mirror_last_idx = defaultdict(int)
        for idx, num in enumerate(nums):
            curr = str(num)
            if curr in mirror_last_idx:
                res = min(abs(mirror_last_idx[curr] - idx) , res)
            mirror_last_idx[str(int(curr[::-1]))] = idx
        return res if res != float("inf") else -1
