class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def get_power(n):
            if n == 1:
                return 0
            if n % 2 == 0:
                return 1 + get_power(n // 2)
            else:
                return 1 + get_power(n * 3 + 1)
        
        power_num = []

        for i in range(lo, hi + 1):
            power_num.append((get_power(i), i))
        
        power_num.sort()

        return power_num[k - 1][1]
        
