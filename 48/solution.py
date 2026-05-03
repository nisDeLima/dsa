class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        l, r = 0, n - 1

        while l < r:
            for i in range(r - l):
                top_left     = [l,     l + i]
                top_right    = [l + i, r]
                bottom_right = [r,     r - i]
                bottom_left  = [r - i, l]

                temp = matrix[top_left[0]][top_left[1]]
                
                matrix[top_left[0]][top_left[1]] = matrix[bottom_left[0]][bottom_left[1]]
                matrix[bottom_left[0]][bottom_left[1]] = matrix[bottom_right[0]][bottom_right[1]]
                matrix[bottom_right[0]][bottom_right[1]] = matrix[top_right[0]][top_right[1]]
                matrix[top_right[0]][top_right[1]] = temp

            l += 1
            r -= 1
