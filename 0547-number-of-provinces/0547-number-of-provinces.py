class UF:
    def __init__(self , n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self , x , y):
        rx , ry = self.find(x) , self.find(y)
        
        if rx == ry: return
        if self.size[rx] < self.size[ry]:
            rx ,ry = ry , rx
        
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        self.count -= 1
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UF(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i , j)
                    
        return uf.count         