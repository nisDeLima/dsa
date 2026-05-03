class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alph = [0] * 26
        for c in sentence:
            curr = ord(c) - ord("a")
            if 0 <= curr <= 26:
                alph[curr] += 1
        for i in alph:
            if i == 0:
                return False
        return True

