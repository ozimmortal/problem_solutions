class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        row ,col = len(mat) , len(mat[0])
        res = [[] for _ in range( row + col - 1) ]

        for r in range(row):
            for c in range(col):
                if (r + c) % 2 == 0 :
                    res[r + c].insert(0, mat[r][c])
                else:
                    res[r + c].append(mat[r][c])
        return [item for sub in res for item in sub ]       
        