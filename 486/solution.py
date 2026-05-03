class Solution_rmvd:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def get_max(i, l, r):
            if l > r:
                return 0
            
            if i % 2 == 0:
                return max(get_max(i + 1, l, r - 1) + nums[r], get_max(i + 1, l + 1, r) + nums[l])
            else:
                return min(get_max(i + 1, l, r - 1), get_max(i + 1, l + 1, r))
        
        points = get_max(0, 0, len(nums) - 1)

        return points >= sum(nums) - points

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def diff(l, r):
            if l > r:
                return 0
            return max(
                nums[l] - diff(l + 1, r),
                nums[r] - diff(l, r - 1)
            )

        return diff(0, len(nums) - 1) >= 0 
