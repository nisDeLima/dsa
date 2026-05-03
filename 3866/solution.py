class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        counter = Counter(nums)
        for num in nums:
            if num % 2 == 0 and counter[num] == 1:
                return num
        return -1
        
