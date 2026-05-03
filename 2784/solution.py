class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_num = max(nums)
        checks = [0] * max_num

        for num in nums:
            checks[num - 1] += 1
        
        for idx, check in enumerate(checks):
            if idx != (max_num - 1) and checks[idx] != 1:
                return False
            elif idx == (max_num - 1) and checks[idx] != 2:
                return False
        
        return True
