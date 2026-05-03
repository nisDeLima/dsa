class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = (nums[i], nums[i + n])
        
        l = n - 1
        
        for i in range(len(nums) - 1, - 1,  -2):
            nums[i] = nums[l][1]
            nums[i - 1] = nums[l][0]
            l -= 1

        return nums
