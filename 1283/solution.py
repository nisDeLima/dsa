class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_valid(candidate):
            result = sum(
                [ math.ceil(num / candidate) for num in nums ]
            )

            return result <= threshold

        left, right = 1, max(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if is_valid(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
