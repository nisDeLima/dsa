class Solution:
    def longestSubarray_removed(self, nums: List[int]) -> int:
        l = 0
        deleted_idx = None
        ans = 0
        for r in range(len(nums)):
            if nums[r] != 1 and deleted_idx == None:
                deleted_idx = r
            elif nums[r] != 1:
                l = deleted_idx + 1
                deleted_idx = r
            curr_size = r - l + 1
            ans = max(curr_size, ans)
        return ans - 1
    
    def longestSubarray(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 2)
        sufix = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            if nums[i] == 1:
                prefix[i + 1] = prefix[i] + nums[i]
            if nums[len(nums) - 1 - i] == 1:
                sufix[len(nums) - i] = sufix[len(nums) - i + 1] + nums[len(nums) - 1 - i]
        ans = max(prefix)
        for i in range(len(nums)):
            if nums[i] == 0:
                ans = max(ans, prefix[i] + sufix[i + 2] + 1)
        return ans - 1
