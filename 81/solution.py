class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)
            if nums[mid] == target:
                return True
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return False
