class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        ans = []

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return

            for j in range(len(nums)):
                if nums[j] not in used:
                    used.add(nums[j])
                    curr.append(nums[j])
                    backtrack(curr)
                    curr.pop()
                    used.remove(nums[j])

        backtrack([])
        return ans
