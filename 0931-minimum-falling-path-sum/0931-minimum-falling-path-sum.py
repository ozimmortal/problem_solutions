class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def valid(x , y):
            return 0 <= x < n and 0 <= y < n
        @cache
        def dp(x , y):
            if not valid(x , y):
                return float('inf')

            if x == n - 1:
                return matrix[x][y]

            return matrix[x][y] + min(dp(x+1 ,y), dp(x + 1 , y -1) , dp(x + 1, y + 1))
        

        n = len(matrix)
        return min(dp(0 , i) for i in range(n)) 
            