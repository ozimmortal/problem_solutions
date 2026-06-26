class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[0] * n for _ in range(n)]
        top , bottom , left , right = 0 , n  , 0 , n
        num = 1

        while num < (n * n) + 1:
            for i in range(left , right):
                res[top][i] = num
                num += 1
            top += 1

            for i in range(top , bottom):
                res[i][right - 1] = num
                num += 1
            right -= 1

            for i in range(right- 1 , left - 1 , -1):
                res[bottom - 1][i] = num
                num +=1
            bottom -= 1

            for i in range(bottom - 1 , top -1 , -1):
                res[i][left] = num
                num += 1
            left += 1 

        return res
