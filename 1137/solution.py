class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = deque([0, 1, 1])
        if n == 0:
            return 0
        if n <= 2:
            return 1

        for i in range(3, n + 1):
            new_num = sum(dp)
            dp.popleft()
            dp.append(new_num)
        
        return dp[-1]

