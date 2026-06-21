
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        m , n = len(grid) , len(grid[0])
        mul = 3
        grid2 = [[0] * (n * mul) for _ in range(m * mul )]

        for r in range(m):
            for c in range(n):
                r2 , c2 = r * mul , c * mul
                if grid[r][c] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2+1] = 1
                    grid2[r2 + 2][c2 + 2] = 1
                
                elif grid[r][c] == "/":
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2+1] = 1
                    grid2[r2 + 2][c2] = 1
    
        def valid(x , y):
            return 0 <= x < m * mul and 0 <= y < n * mul 

        def dfs(r , c):
            
            for dx , dy in directions:
                nx , ny = r + dx , c + dy
                if valid(nx , ny) and grid2[nx][ny] == 0 and (nx , ny) not in seen:
                    seen.add((nx , ny))
                    dfs(nx , ny)

        directions = [(1, 0) , (0 , 1) , (-1 ,0) ,(0, -1)]
        seen = set()
        res = 0

        for r in range(m * mul):
            for c in range(n * mul):
                if grid2[r][c] == 0 and (r , c) not in seen:
                    seen.add((r , c))
                    dfs(r ,c)
                    res += 1

        return res