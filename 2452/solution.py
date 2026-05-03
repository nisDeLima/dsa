class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []

        def compare(w1, w2):
            diff = 0

            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
                    if diff > 2:
                        return False

            return True

        for word in queries:
            for target in dictionary:
                if compare(word, target):
                    res.append(word)
                    break

        return res
