class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_s = prices[0]

        for stock in prices[1::]:
            res = max(res, stock - min_s)
            min_s = min(min_s, stock)

        return res
