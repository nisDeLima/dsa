class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)

        res = self.myPow(x, n // 2)
        if n % 2 == 0:
            return res * res
        return res*res*x
