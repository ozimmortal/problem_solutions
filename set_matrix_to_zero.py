class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        j = []
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    j.append([r,c])
                    
        for r,c in j:
            # update the row 
            for uc in range(len(matrix[r])):
                matrix[r][uc] = 0
                # update the column
            for ur in range(len(matrix)):
                matrix[ur][c] = 0
                

            






        