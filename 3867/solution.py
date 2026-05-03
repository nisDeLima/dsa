class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        mx = nums[0]

        for num in nums:
            mx = max(mx, num)
            prefix_gcd.append(math.gcd(mx, num))

        prefix_gcd.sort()
        res = 0
        l, r = 0, len(prefix_gcd) - 1

        while l < r:
            res += math.gcd(prefix_gcd[l], prefix_gcd[r])
            l += 1
            r -= 1

        return res
