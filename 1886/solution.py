class Solution_rmvd:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        curr = mat
        for _ in range(4):
            next_mat = [[0] * len(mat) for _ in range(len(mat[0]))]
            for row in range(len(mat)):
                for col in range(len(mat[0])):
                    elm = curr[row][col]
                    next_mat[col][len(mat[0]) - row - 1] = elm
            if next_mat == target:
                return True
            curr = next_mat
        
        return False
            
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        for _ in range(4):
            if mat == target:
                return True
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for row in mat:
                row.reverse()

        return False
