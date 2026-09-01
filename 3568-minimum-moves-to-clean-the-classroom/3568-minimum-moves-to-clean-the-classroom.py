class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        
        def val(x ,y): return 0 <= x < m and 0 <= y < n

        m , n = len(classroom), len(classroom[0])
        directions = [(1, 0),(0, 1),(-1,0),(0,-1)]
        start, litters = (0 , 0), {}
        for x in range(m):
            for y in range(n):
                if classroom[x][y] == "S":
                    start = (x , y)
                elif classroom[x][y] == "L":
                    litters[(x, y)] = len(litters)
        target = (1 << len(litters)) - 1
        queue = deque([(start[0], start[1], 0 , 0 , energy)])
        seen = {(start[0], start[1], 0) : energy}
        while queue:
            x , y , s , mask , e = queue.popleft()
           
            if mask == target: return s
            if e == 0: continue

            for dx, dy in directions:
                nx , ny = x + dx , y + dy
                if val(nx , ny) and classroom[nx][ny] != "X":
                    newE = e - 1
                    newM = mask
                    grid = classroom[nx][ny]
                   
                    if grid == "R":
                        newE = energy
                    if grid == "L":
                        idx = litters[(nx ,ny)]
                        newM |= 1 << idx
                    
                    if newM == target : return s + 1
                    
                    state = (nx , ny, newM)
                    if state not in seen or newE > seen[state]:
                        queue.append((nx , ny , s + 1 , newM, newE))
                        seen[state] = newE

        return -1



