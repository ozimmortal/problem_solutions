class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        self.res = 0
        self.obstacle = set()

        def valid(r ,c):
            return 0 <= r < m and 0 <= c < n

        def dfs(node ,seen):
            
            x , y = node
            if grid[x][y] == 2 :
                if len(seen) == (m * n) - len(self.obstacle):
                    self.res += 1
                return
            directions = [(0 ,1) , (1, 0) , (-1 , 0), (0 , -1)]
            for dx ,dy in directions:
                nx , ny = x + dx , y + dy
                
                if valid(nx , ny) and (nx , ny) not in seen:
                    if grid[nx][ny] == -1:
                        self.obstacle.add((nx , ny))
                        continue
                    seen.add((nx ,ny))
                    dfs((nx, ny), seen)
                    seen.remove((nx, ny))
                


        m , n = len(grid) , len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    seen = {(row , col)}
                    dfs((row , col) , seen)
                    break
        return self.res