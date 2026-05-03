class Solution_rmvd:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        best = float("-inf")

        for l in range(len(nums) - firstLen + 1):
            first_window = prefix[l + firstLen] - prefix[l]
            for s_l in range(len(nums) - secondLen + 1):
                if s_l < l + firstLen and s_l + secondLen > l:
                    continue
                second_window = prefix[s_l + secondLen] - prefix[s_l]
                best = max(best, first_window + second_window)

        return best
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def solve(left_len, right_len):
            best = 0
            best_left = 0
            for i in range(left_len + right_len - 1, len(nums)):
                right_start = i - right_len + 1
                left_start = right_start - left_len
                best_left = max(best_left, prefix[left_start + left_len] - prefix[left_start])
                best = max(best, best_left + prefix[right_start + right_len] - prefix[right_start])
            return best

        return max(solve(firstLen, secondLen), solve(secondLen, firstLen))
