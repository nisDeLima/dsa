class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discounts_stack = [0]
        res = []
        for num in reversed(prices):
            while num < discounts_stack[-1]:
                discounts_stack.pop()
            res.append(num - discounts_stack[-1])
            discounts_stack.append(num)
        return list(reversed(res))
