class Solution:
    def canBeIncreasing_rmv(self, nums: List[int]) -> bool:
        def custom_sort_check(ignore_idx):
            prev = float("-inf")
            for i in range(len(nums)):
                if nums[i] <= prev and i != ignore_idx:
                    return False
                elif i != ignore_idx:
                    prev = nums[i]

            return True
        
        for try_ignore in range(len(nums)):
            if custom_sort_check(try_ignore):
                return True
        
        return False
    def canBeIncreasing(self, nums: List[int]) -> bool:
        r=False
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                if r:
                    return False
                if i>1 and nums[i]<=nums[i-2]:
                    nums[i]=nums[i-1]
                r=True
        return True
        
