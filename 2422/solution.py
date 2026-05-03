class Solution:
    def minimumOperations_ttl(self, nums: List[int]) -> int:
        def dp(left, right):
            if left == right:
                return 0

            equal_path = float("inf")
            sum_left = float("inf")
            sum_right = float("inf")

            if nums[left] == nums[right]:
                equal_path = dp(left + 1, right - 1)
            else: 
                nums[left + 1] += nums[left]
                sum_left = 1 + dp(left + 1, right)
                nums[left + 1] -= nums[left]

                nums[right - 1] += nums[right]
                sum_right = 1 + dp(left, right - 1)
                nums[right - 1] -= nums[right]

            return min(equal_path, sum_left, sum_right)

        return dp(0, len(nums) - 1)

    def minimumOperations(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ops = 0

        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                nums[left + 1] += nums[left]
                left += 1
                ops += 1
            else:
                nums[right - 1] += nums[right]
                right -= 1
                ops += 1

        return ops

