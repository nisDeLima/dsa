class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []

        for i in range((len(nums) - 1) * 2, - 1, - 1):
            i = i % (len(nums))
            num = nums[i]
            while stack and stack[-1] <= num:
                stack.pop()
            if stack and res[i] == -1:
                res[i] = stack[-1]
            stack.append(num)
        return res
