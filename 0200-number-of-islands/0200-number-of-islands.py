class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def valid(r , c):
            return 0 <= r < m and 0 <= c < n
        
        def dfs(node):

            r , c = node
            directions = [(0 , 1), (1 , 0) ,(-1 , 0), (0, -1)]
            
            if grid[r][c] == "0":
                return 

            for dx ,dy in directions:
                nr ,nc = r + dx , c + dy
                if valid(nr ,nc) and grid[nr][nc] == "1" and (nr , nc ) not in seen: 
                    seen.add((nr , nc))
                    dfs((nr ,nc))
           
        
        m , n = len(grid) , len(grid[0])
        seen= set()
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r ,c) not in seen:
                    seen.add((r ,c))
                    dfs((r,c))
                    count += 1

        return count