class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_arr = []
        curr = 0
        r = 0

        for i in range(len(nums)):
            curr = nums[i]
            sum_arr.append(curr)
            for j in range(i + 1, len(nums)):
                curr += nums[j]
                sum_arr.append(curr)

        sum_arr.sort()

        for l in range(left - 1, right):
            r += sum_arr[l]

        return r % (10 ** 9 + 7)
