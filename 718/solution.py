class Solution:
    def findLength_rmv(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def rec(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0
            
            if nums1[i] == nums2[j]:
                return 1 + rec(i + 1, j + 1)
            return 0
        
        # Try all starting positions
        max_len = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                max_len = max(max_len, rec(i, j))
        
        return max_len

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_len = max(max_len, dp[i][j])
        
        return max_len
