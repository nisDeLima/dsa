class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # Prefix count for each of 26 possible characters
        prefix = [[0] * (n + 1) for _ in range(26)]
        
        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            for c in range(26):
                prefix[c][i + 1] = prefix[c][i]
            prefix[char_idx][i + 1] += 1
        
        res = []
        for l, r in queries:
            count = 0
            for c in range(26):
                freq = prefix[c][r + 1] - prefix[c][l]
                if freq > 0:
                    count += freq * (freq + 1) // 2
            res.append(count)
        
        return res
