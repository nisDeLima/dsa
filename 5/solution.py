class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_mid(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return l + 1, r - 1
        

        res = [0, 0]
        for i in range(len(s)):
            candl, candr = expand_from_mid(i, i)

            if (candr - candl + 1) > (res[1] - res[0] + 1):
                res = [candl, candr]

            candl, candr = expand_from_mid(i, i + 1)

            if (candr - candl + 1) > (res[1] - res[0] + 1):
                res = [candl, candr]
        
        return s[res[0]:res[1] + 1]
