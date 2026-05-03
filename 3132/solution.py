class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        # Try all possible first elements from nums1 (we can remove at most 2)
        # The valid cand must be nums2[0] - nums1[i] for i = 0, 1, 2
        ans = float('inf')
        
        for i in range(3):
            cand = nums2[0] - nums1[i]
            
            # Verify if this cand works
            j = 0  # pointer for nums2
            removed = 0  # number of elements removed from nums1
            
            for num in nums1:
                if j < len(nums2) and num + cand == nums2[j]:
                    j += 1
                else:
                    removed += 1
                    if removed > 2:
                        break
            
            if j == len(nums2):
                ans = min(ans, cand)
        
        return ans
