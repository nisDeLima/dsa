class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            prefix_sum += nums[i]
            res = max(math.ceil(prefix_sum / (i + 1)), res)
        return resclass Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            prefix_sum += nums[i]
            res = max(math.ceil(prefix_sum / (i + 1)), res)
        return res
