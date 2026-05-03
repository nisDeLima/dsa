class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0
        nums.sort() 

        l = 0
        res = float("inf")
        for r in range(k - 1, len(nums)):
            res = min(res, nums[r] - nums[l])
            l += 1
        return res
