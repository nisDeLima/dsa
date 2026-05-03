class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = 0

        max_idx = -1

        for idx, flip in enumerate(flips):
            max_idx = max(flip, max_idx)
            if idx + 1 == max_idx:
                res += 1
        return res
