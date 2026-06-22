class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size   = [1] * n
        self.counts = n

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
        self.counts -= 1

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        equal_uf = UF(26)
        unequal_uf = UF(26)
        equations.sort(key=lambda x :x[1:3] ,reverse=True)
        for eq in equations:
            
            v1 , comp , v2 = eq[0], eq[1:3] , eq[-1]
            ds = ord('a')
            
            x , y = ord(v1) - ds , ord(v2) - ds
            if comp == "!=" and equal_uf.find(x) == equal_uf.find(y):
                print(x , y , comp)
                return False
            if comp == "==" and unequal_uf.find(x) == unequal_uf.find(y) and x != y:
                print(x , y , comp)
                return False
            
            if comp  == "==":
                equal_uf.union(x , y)
            else:
                unequal_uf.union(x , y)
            
        
        return True



        