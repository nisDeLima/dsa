class Solution_rmvd:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [(float("inf"), float("-inf"), 0)] * n
        
        curr = 0
        min_neg = float("inf")
        max_pos = float("-inf")

        for i in range(n):
            curr += nums[i]
            prefix[i] = (min_neg, max_pos, curr)
            
            if curr > 0:
                max_pos = max(max_pos, curr)
            elif curr < 0:
                min_neg = min(min_neg, curr)
        
        res = 0

        for min_before, max_before, curr in prefix:
            res = max(res, abs(curr))
            
            if curr > 0 and min_before != float("inf"):
                res = max(res, curr - min_before)
            if curr < 0 and max_before != float("-inf"):
                res = max(res, max_before - curr)
        
        return res

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_max = 0
        min_min = 0
        curr_max = 0
        curr_min = 0

        for num in nums:
            curr_max = max(0, curr_max + num)
            curr_min = min(0, curr_min + num)
            max_max= max(max_max, curr_max)
            min_min= min(min_min, curr_min)
            
        return max(max_max, abs(min_min))
