class Solution:
    def judgeSquareSum_OOO(self, c: int) -> bool:
        @cache
        def calc(a, b):
            res = a ** 2 + b ** 2
            if res == c:
                return True
            if res > c:
                return False
            
            return calc(a, b + 1) or calc(a + 1, b)
        return cacl(0, 0)
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))


        while l <= r:
            curr = l ** 2 + r ** 2
            if curr == c:
                return True
            elif curr > c:
                r -= 1
            elif curr < c:
                l += 1
        return False

    def judgeSquareSum_t(self, c: int) -> bool:
        sums = set()
        for i in range(int(sqrt(c)) + 1):
            sums.add(c - (i ** 2))
            if (i ** 2) in sums:
                return True
        return False
