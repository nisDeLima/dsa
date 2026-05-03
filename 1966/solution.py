class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        greater_prefix = []
        prev_max = float("-inf")
        for i in range(len(nums)):
            prev_max = max(prev_max, nums[i])
            if nums[i] < prev_max:
                greater_prefix.append(False)
            else:
                greater_prefix.append(True)

        count = 0

        prev_smaller = float("inf")
        for i in range(len(nums) - 1, -1, -1):
            prev_smaller = min(prev_smaller, nums[i])
            if nums[i] <= prev_smaller and greater_prefix[i]:
                count += 1

        return count
