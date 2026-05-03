class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        p2w = {}
        used = set()

        for p, w in zip(pattern, words):
            if p in p2w:
                if p2w[p] != w:
                    return False
            else:
                if w in used:
                    return False
                p2w[p] = w
                used.add(w)

        return True

