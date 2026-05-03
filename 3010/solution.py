class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = nums[0]
        take_two = []

        for i in range(1, len(nums)):
            if len(take_two) < 2:
                take_two.append(nums[i])
            else:
                take_two.sort()
                if nums[i] < take_two[-1]:
                    take_two.pop()
                    take_two.append(nums[i])
        res += sum(take_two)
        return res
