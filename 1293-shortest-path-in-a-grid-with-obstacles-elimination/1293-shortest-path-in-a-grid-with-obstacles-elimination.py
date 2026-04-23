class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        #               x   y   s   v->k
        queue = deque([(0 , 0 , 0 , k)])
        seen = {(0 , 0 , k)}
        directions = [(1,0) , (0, 1) , (-1 , 0), (0, -1)]
        m , n = len(grid) , len(grid[0])

        def valid(x , y):
            return 0 <= x < m and 0 <= y < n

        while queue:
            x , y , s , v = queue.popleft()

            if x == m -1 and y == n-1:
               return s
            
            for dx , dy in directions:
                nx , ny = x + dx , y + dy
                if valid(nx , ny) and (nx , ny , v) not in seen:

                    if grid[nx][ny] == 0:
                        queue.append((nx , ny , s + 1 , v))
                        seen.add((nx ,ny , v))
                        continue

                    if grid[nx][ny] == 1 and v > 0:
                        queue.append((nx , ny , s + 1 , v - 1))
                        seen.add((nx ,ny , v - 1))
                        continue

                    
        return -1
                        
