class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        universal_set = set() 
        for i in range(len(s) - k + 1):
            universal_set.add(s[i:i+k])
        return len(universal_set) == 2 ** k

