class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        p2 = 0
        for p1 in range(len(nums1)):
            p2 = max(p1, p2)
            while p2 < len(nums2) and nums1[p1] <= nums2[p2]:
                p2 += 1
            res = max(res, p2 - 1 - p1)
        return res
