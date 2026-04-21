class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def valid(x,y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x , y):

            area = 0
            directions= [(1 , 0) , (0 , 1) , (-1 , 0), (0 ,-1)]
            # print( area , x ,y ,seen)
            if grid[x][y] == 0:
                return 0
            if  grid[x][y] == 1:
                seen.add((x , y))
                area += 1

            for dx , dy in directions:
                nx ,ny = x + dx , y + dy
                if valid(nx, ny) and  (nx , ny) not in seen:
                    area += dfs(nx ,ny)

            return area

        m , n = len(grid) , len(grid[0])
        seen = set()
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row ,col) not in seen:
                    # seen.add((row ,col))
                    ans = max(ans ,dfs(row ,col))
                    
                    
                
        return ans

            