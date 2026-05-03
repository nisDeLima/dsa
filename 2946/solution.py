class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n
        if k == 0:
            return True
        for row in mat:
            for i in range(n):
                if row[i] != row[(i + k) % n]:
                    return False
        return True
