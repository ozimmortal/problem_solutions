class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c_m = [x.copy() for x in matrix]
        n = len(matrix)
        m = n - 1
        for c in range(n):
            for r in range(n):
                matrix[r][c] = c_m[m][r]
            m -= 1
        

