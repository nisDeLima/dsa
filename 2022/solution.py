class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        res = [([0] * n) for _ in range(m)]
        
        i = 0
        for row in range(m):
            for col in range(n):
                res[row][col] = original[i]
                i += 1
        
        return res

