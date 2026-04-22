class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid) 
        def valid(x ,y):
            return 0 <= x < n and 0 <= y < n

        if grid[0][0] != 0 or grid[n-1][n-1]:
            return -1

        queue = deque([(0 , 0 , 0)])
        seen = {(0 , 0)}
        
        while queue:
            x , y , ans = queue.popleft()
            directions = [(1 , 1), (1 , -1), (-1 ,1) ,(-1 , -1) ,(0 , 1) , (1, 0) , (-1, 0) , (0 , -1) ]
            if x == n- 1 and y == n -1:
                return ans + 1
            
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if valid(nx , ny) and grid[nx][ny] == 0 and (nx ,ny) not in seen:
                    seen.add((nx ,ny))
                    queue.append((nx , ny , ans + 1))
            
        return -1
        