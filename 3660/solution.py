class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        ans = []
        curr = float('-inf')
        
        for num in nums:
            curr = max(curr, num)
            ans.append(curr)
        
        curr = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if ans[i] > nums[curr]:
                ans[i] = ans[curr]
            if nums[i] < nums[curr]:
                curr = i
        return ans
