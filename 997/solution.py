class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        trust_target = n

        trust_data = [[0, 0] for _ in range(n + 1)] # index is the person, [a, b] a = number of people they trust, b = number of people trusting in them

        for a, b in trust:
            trust_data[b][1] += 1
            trust_data[a][0] += 1
        
        for idx, (trusting, trust_count) in enumerate(trust_data):
            if trusting == 0 and trust_count == n - 1:
                return idx
        
        return -1

