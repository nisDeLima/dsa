class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_map = {}
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                next_map[num] = stack[-1]
            else:
                next_map[num] = -1
            stack.append(num)

        return [next_map[num] for num in nums1]
