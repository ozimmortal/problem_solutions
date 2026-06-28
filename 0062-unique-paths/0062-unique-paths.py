class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def valid(x , y):
            return 1 <= x <= m and 1 <= y <= n
        
        memo = {}
        def dp(x , y):
            if x == m and y == n:
                return 1
            
            directions = [(0 , 1) , (1 , 0)]
            count = 0

            for dx ,dy in directions:
                nx ,ny = x + dx ,  y + dy
                if (nx , ny) in memo:
                    count += memo[(nx, ny)]
                    continue
                
                if valid(nx ,ny):
                    memo[(nx , ny)] = dp(nx , ny)
                    count += memo[(nx, ny)]
            
            return count

        return dp(1 , 1)
