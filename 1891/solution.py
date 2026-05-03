class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def validate(candidate):
            count = 0
            for ribbon in ribbons:
                count += ribbon // candidate
                if count >= k:
                    return True
            return False

        l, r = 1, max(ribbons)

        while l <= r:
            mid = (l + r) // 2
            if validate(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r
