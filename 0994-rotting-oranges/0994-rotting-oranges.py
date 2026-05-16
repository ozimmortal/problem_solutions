class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def valid(x , y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        m , n = len(grid) , len(grid[0])
        queue = deque()
        seen = set()
        oranges = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    oranges+=1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r , c , 0 ,oranges))
                    seen.add((r ,c))
                

        directions = [(1 , 0 ), (0 , 1) , (-1 , 0) , (0 , -1)]
        while queue:
            x , y , time, o = queue.popleft()
            if o == 0:
                return time
            nodes = []
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if valid(nx ,ny) and (nx , ny) not in seen:
                    oranges -= 1
                    nodes.append((nx ,ny , time + 1))
                    seen.add((nx ,ny))
            for node in nodes:
                queue.append((*node , oranges))
                    

        return -1 if oranges > 0 else 0


         

        