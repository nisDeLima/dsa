class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        for num in nums[1:]:
            insert_idx = bisect_left(lis, num)
            if insert_idx == len(lis):
                lis.append(num)
            else:
                lis[insert_idx] = num
        return len(lis)
