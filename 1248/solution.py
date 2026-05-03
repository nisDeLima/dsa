class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = []
        curr = 1
        for num in nums:
            if num % 2 != 0:
                prefix.append(curr)
                curr = 1
            else:
                curr += 1

        suffix = []
        curr = 1
        for num in reversed(nums):
            if num % 2 != 0:
                suffix.append(curr)
                curr = 1
            else:
                curr += 1
        suffix.reverse()

        res = 0
        for i in range(len(prefix) - k + 1):
            res += prefix[i] * suffix[i + k - 1]
        return res
