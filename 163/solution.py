class Solution:
    def findMissingRanges_rmvd(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ranges = []
        nums_set = set(nums)

        curr_range = []
        for num in range(lower, upper + 1):
            if num not in nums_set:
                if len(curr_range) == 0:
                    curr_range = [num, num]
                else:
                    curr_range[1] = num
            elif len(curr_range) == 2:
                ranges.append(curr_range.copy())
                curr_range = []
        if curr_range:
            ranges.append(curr_range.copy())
        return ranges
    
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        ranges = []
        left = lower - 1
        for num in nums:
            if num > left + 1:
                ranges.append([left + 1, num - 1])
            left = num
        if left < upper:
            ranges.append([left + 1, upper])
        return ranges
