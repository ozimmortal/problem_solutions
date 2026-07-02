class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        @cache
        def dp(i , j):
            if i == len(triangle) or j == len(triangle):
                return 0
            
            return min(triangle[i][j] + dp(i + 1 , j) , triangle[i][j] + dp(i + 1 , j + 1 ))
        
        return dp(0 , 0)