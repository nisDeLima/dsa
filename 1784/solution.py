class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0

        i = 0

        while i < len(s):
            if s[i] == "1":
                count += 1
                while i < len(s) and s[i] == "1":
                    i += 1
            i += 1
        
        return count <= 1
