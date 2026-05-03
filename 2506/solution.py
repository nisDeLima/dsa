class Solution:
    def similarPairs(self, words: List[str]) -> int:
        patterns = defaultdict(int)
        res = 0

        for word in words:
            if frozenset(word) in patterns:
                res += patterns[frozenset(word)]
            patterns[frozenset(word)] += 1
        return res
