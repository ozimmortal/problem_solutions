class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t_matrix = []
        for i in range(len(matrix[0])):
            e =[]
            for j in range(len(matrix)):
                e.append(matrix[j][i])
            t_matrix.append(e)
        return t_matrix

