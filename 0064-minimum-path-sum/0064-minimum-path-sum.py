class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        @cache
        def dp(r ,c):
            if r == m -1 and c == n - 1:
                return grid[r][c]

            ans = float('inf')  
            if 0 <= r < m and  0<= c < n:
                ans = min(ans, grid[r][c] + dp(r , c + 1 ) , grid[r][c] + dp(r+1 , c))
            
            return ans

        m , n = len(grid) , len(grid[0])
        return dp(0 , 0)

