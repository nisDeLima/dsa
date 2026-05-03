class Solution:
    def maxScore_remove(self, cardPoints: List[int], k: int) -> int:
        @cache
        def dfs(l, r, k):
            if l  > r or k == 0:
                return 0
            take_left = cardPoints[l] + dfs(l + 1, r, k - 1)
            take_right = cardPoints[r] + dfs(l, r - 1, k - 1)
            return max(take_left, take_right)
        return dfs(0, len(cardPoints) - 1, k) 

    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        left_sum = sum(cardPoints[:k])
        res = left_sum
        right_sum = 0

        for i in range(1, k + 1):
            left_sum -= cardPoints[k - i]
            right_sum += cardPoints[-i]
            res = max(res, left_sum + right_sum)

        return res
