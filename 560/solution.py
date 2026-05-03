class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1

        total = 0
        result = 0

        for x in nums:
            total += x
            result += counts[total - k]
            counts[total] += 1

        return result
