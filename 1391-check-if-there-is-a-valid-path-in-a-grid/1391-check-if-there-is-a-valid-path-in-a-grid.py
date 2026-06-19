class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size   = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry]  = rx
        self.size[rx]   += self.size[ry]

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        if grid[0][0] == 5:
            return False
        
        roads = {
            1 : [(0 , 1) , (0 , -1)],
            2 : [(1 , 0) , (-1 , 0)],
            3 : [(0 , -1) , (1 , 0)],
            4 : [(0 , 1) , (1 , 0)],
            5 : [(0 , -1) , (-1 , 0)],
            6 : [(0 , 1) , (-1 , 0)]
        }
        
        def valid(x , y):
            return 0 <= x < m and 0 <= y < n
        
        def idx(x ,y):
            return x * n + y
        
        m , n = len(grid) , len(grid[0])
        uf = UF(m * n)

        for r in range(m):
            for c in range(n):
                street = grid[r][c]

                for dx , dy in roads[street]:
                    nr , nc = r + dx , c + dy

                    if not valid(nr , nc):
                        continue
                    
                    if (-dx , -dy) in roads[grid[nr][nc]]:
                        uf.union(idx(r , c),idx(nr , nc))

        last = (m * n) - 1
        return uf.find(0) == uf.find(last) 
        