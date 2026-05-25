class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        def valid(x ,y):
            return 0 <= x < m and 0 <= y < n

        ans = -1
        m , n = len(grid) , len(grid[0])
        directions = [(1, 0), (0 , 1) , (-1 , 0), (0 , -1)]
        queue = deque([ (x , y , 0) for x in range(m) for y in range(n) if grid[x][y]])
        seen = {(x , y ) for x in range(m) for y in range(n) if grid[x][y]}
        
        while queue:
            x , y , d = queue.popleft()
            if grid[x][y]  == 0:
                ans = max(ans , d)

            
            for dx ,dy in directions:
                nx ,ny = x + dx , y + dy
                if valid(nx , ny)  and (nx ,ny) not in seen:
                    queue.append((nx ,ny , d + 1))
                    seen.add((nx ,ny))
        return ans
            
