class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()

        res = 0

        def check(i):
            l, r = i + 1, len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[i] + nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return max(r - i, 0)

        for i in range(len(nums)):
            res += check(i)

        return res

