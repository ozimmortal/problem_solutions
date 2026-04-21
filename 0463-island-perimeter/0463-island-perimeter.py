class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def valid(x , y):
            return 0 <= x < m and 0 <= y < n 
        def cal_perimeter(x ,y):
            p = 0
            for dx ,dy in directions:
                nx , ny = dx + x , dy + y
                if not valid(nx ,ny) or (valid(nx ,ny) and grid[nx][ny] == 0):
                    p += 1
            return p
        
        def dfs(node):
            x , y = node
    
            for dx , dy in directions:
                nx , ny = dx + x , dy + y
                if valid(nx ,ny) and (nx , ny) not in seen and grid[nx][ny] == 1:
                    seen.add((nx , ny))
                    dfs((nx,ny))
        
        seen = set()
        m , n = len(grid) , len(grid[0])
        directions = [(0 , 1), (1 , 0) , (-1 , 0), (0 , -1)]
        for row in range(m):
            for col in range(n):
                node = (row , col)
                if grid[row][col] == 1 and node not in seen:
                    seen.add(node)
                    dfs(node)
        
        print(seen)
        perimeter = 0
        for x ,y in seen:
            perimeter += cal_perimeter(x ,y)
        
        return perimeter



        