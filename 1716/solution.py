class Solution:
    def totalMoney(self, n: int) -> int:
        w, r = divmod(n, 7)

        total_weeks = 28*w + 7*(w-1)*w//2
        total_rest  = r*w + r*(r+1)//2

        return total_weeks + total_rest
