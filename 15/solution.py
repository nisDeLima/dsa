class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        L = len(nums)
        triplets = []

        for i in range(L - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates for i

            left, right = i + 1, L - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left_val, right_val = nums[left], nums[right]
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return triplets
