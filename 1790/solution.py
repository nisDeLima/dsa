class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        ord1 = [0] * 26        
        ord2 = [0] * 26        

        for c in s1:
            ord1[ord(c) - ord("a")] += 1

        for c in s2:
            ord2[ord(c) - ord("a")] += 1
        
        if ord1 != ord2:
            return False

        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
            if diff > 2:
                return False

        return True

