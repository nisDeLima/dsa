class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all zeroes to the end in-place, keeping order of non-zero elements.
        O(n) time, O(1) space.
        """
        insert_pos = 0

        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

