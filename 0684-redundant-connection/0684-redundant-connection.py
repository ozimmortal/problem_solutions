class UF:
    def __init__(self , n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self , x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self , x , y):
        px , py = self.parent[x] , self.parent[y]

        if px == py: return
        if self.size[px] < self.size[py]:
            px , py = py , px
        
        self.parent[py] = px
        self.size[px] += self.size[py]
    

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf  = UF(n + 1)

        for x , y in edges:
            if uf.find(x) != uf.find(y):
                uf.union(x ,y)
            else:
                return [x ,y]
        
