class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def valid(x , y):
            return 0 <= x < m and 0 <= y < n and obstacleGrid[x][y] == 0 

        @cache
        def dp(x ,y):

            if x == m - 1 and y == n -1:
                return 1 if valid(x , y) else 0

            ways = 0
            if valid(x , y):
                ways += dp(x + 1 , y) + dp(x , y + 1)

            return ways 


        m , n = len(obstacleGrid) , len(obstacleGrid[0])
        return dp(0 , 0)