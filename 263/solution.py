class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        for d in [2,3,5]:
            while n%d==0:
                n=n/d
        return n==1
        
