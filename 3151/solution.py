class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        curr = 0
        l = 0
        for i in range(len(nums)):
            curr += nums[i]
            if i >= 2:
                curr -= nums[l]
                l += 1
            if i >= 1 and curr % 2 == 0:
                return False
        return True
