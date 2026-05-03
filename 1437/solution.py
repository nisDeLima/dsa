class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        last_one_idx = None

        for idx, num in enumerate(nums):
            if num and last_one_idx != None:
                if idx - last_one_idx - 1 < k:
                    return False
                last_one_idx = idx
            elif num:
                last_one_idx = idx
        return True
