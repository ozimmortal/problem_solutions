class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def valid(x , y):
            return 0 <= x  <m and 0 <= y <n

        def onboundary(x , y):
            return (x == 0 or x == m - 1) or (y == 0 or y == n-1)

        def dfs(x ,y):
            count = 1
            if onboundary(x , y):
                self.isSurrounded = False
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if valid(nx , ny) and (nx , ny) not in seen and grid[nx][ny] == 1:
                    seen.add((nx, ny))
                    count += dfs(nx , ny)
            return count

        m , n = len(grid) , len(grid[0])
        directions = [(1 , 0) , (0 , 1), (-1 , 0), (0, -1)]
        seen = set()
        res = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r , c) not in seen:
                    self.isSurrounded = True
                    seen.add((r, c))
                    count = dfs(r , c)
                    if self.isSurrounded:
                        res += count
        return res

        
