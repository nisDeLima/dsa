class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            while i < len(nums) -1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        backtrack(0)
        return ans 
