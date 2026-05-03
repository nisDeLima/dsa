class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1

        for l in range(n):
            prod = 1
            g = 0
            c = 1
            for r in range(l, n):
                x = nums[r]

                prod *= x
                g = x if g == 0 else gcd(g, x)
                c = lcm(c, x)

                if prod == g * c:
                    res = max(res, r - l + 1)

        return res

