class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row , col = len(img) , len(img[0])
        result  = [[0] * col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                count , total = 0 , 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1 ,c + 2):
                        if 0 <= i < row and 0 <= j < col:
                            total += img[i][j]
                            count += 1
                result[r][c] = total // count 
        return result

        