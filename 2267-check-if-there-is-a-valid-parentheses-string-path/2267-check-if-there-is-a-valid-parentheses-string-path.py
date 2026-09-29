class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        
        def valid(x , y):
            return 0 <= x < m and 0 <= y < n
        
        if grid[0][0] == ")": return False

        m , n = len(grid) , len(grid[0])
        directions = [(1 , 0) , (0 , 1)]
        queue = deque([(0 , 0, 1)])
        seen = {(0 , 0 , 1)}
        while queue:
            x , y , c = queue.popleft()

            if x ==  m - 1 and y == n - 1:
                if c == 0:
                    return True
                continue

            for dx , dy  in directions:
                nx , ny = x + dx , y + dy
                if valid(nx , ny):
                    new_c = c
                    if grid[nx][ny] == "(":
                        new_c  += 1
                    else:
                        new_c -= 1
                    
                    if new_c < 0 or (nx , ny , new_c) in seen:
                        continue
                    queue.append((nx , ny , new_c))
                    seen.add((nx , ny , new_c))
            
        return False
