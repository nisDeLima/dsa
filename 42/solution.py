class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        max_r = height[-1]
        max_l = height[0]

        l, r = 0, len(height) - 1

        while l < r:
            if max_r <= max_l:
                r -= 1
                ans += max(max_r - height[r], 0)
                max_r = max(max_r, height[r])
            else:
                l += 1
                ans += max(max_l - height[l], 0)
                max_l = max(max_l, height[l])
        return ans


