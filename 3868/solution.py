class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        diff1 = 0
        diff2 = 0
        if counter1 == counter2:
            return 0
        else:
            for key, cnt in (counter1 - counter2).items():
                if cnt % 2 != 0:
                    return -1
                diff1 += cnt // 2
            for key, cnt in (counter2 - counter1).items():
                if cnt % 2 != 0:
                    return -1
                diff2 += cnt // 2
        return diff1 if ((diff1 - diff2) == 0) else -1
              
