class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        L = len(nums)
        MAX = max(nums)

        res = 0
        curr_count = 0
        l = 0
        for r in range(L):
            if nums[r] == MAX:
                curr_count += 1
            while curr_count == k:
                res += 1 + (L - r - 1)
                if nums[l] == MAX:
                    curr_count -= 1
                l += 1
        return res
