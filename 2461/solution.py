class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        L = len(nums)

        if L < k:
            return 0

        seen = set()
        res = 0
        curr_sum = 0
        l = 0
        for r in range(L):
            while nums[r] in seen or r - l + 1 > k:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1

            seen.add(nums[r])
            curr_sum += nums[r]

            if r - l + 1 == k:
                res = max(res, curr_sum)

        return res
