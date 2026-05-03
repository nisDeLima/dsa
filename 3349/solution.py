class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        increasing = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing[i] = increasing[i - 1] + 1

        for i in range(len(increasing) - k):
            if increasing[i] >= k and increasing[i + k] >= k:
                return True

        return False
