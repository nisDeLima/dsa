class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_ord = [0] * 26
        magazine_ord = [0] * 26

        for char in ransomNote:
            curr_ord = ord(char) - ord("a")
            ransom_ord[curr_ord] += 1

        for char in magazine:
            curr_ord = ord(char) - ord("a")
            magazine_ord[curr_ord] += 1

        for i in range(26):
            if magazine_ord[i] < ransom_ord[i]:
                return False

        return True
