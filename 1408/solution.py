class Solution:
    def stringMatching_tes(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        res = []

        def is_sub(w1, w2):
            for i in range(len(w2)):
                p1, p2 = 0, i
                while p1 < len(w1) and p2 < len(w2) and w1[p1] == w2[p2]:
                    p2 += 1
                    p1 += 1
                if p1 == len(w1):
                    return True
            return False

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if is_sub(words[i], words[j]):
                    res.append(words[i])
                    break
            
        return res
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, word in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if word in word2:
                    res.append(word)
                    break
        return res
