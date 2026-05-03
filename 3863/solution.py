class Solution:
    def minOperations(self, s: str) -> int:
        if all(s[i]<=s[i+1] for i in range(len(s)-1)):
            return 0

        if len(s) == 2:
            return -1

        mini = min(s)
        maxi = max(s)

        if s[0] == mini or s[-1] == maxi:
            return 1

        if(s[0] == maxi and s.count(maxi) == 1 and s[-1] == mini and s.count(mini) == 1):
            return 3
        return 2
        
