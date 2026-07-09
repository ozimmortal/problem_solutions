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
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        uf = UF(n)
        for i in range(1 , n):
            diff = nums[i] - nums[i - 1]
            if diff <= maxDiff:
                uf.union(i-1 ,i)
            
        
        res =[]
        for l ,r in queries:
            st = False
            if uf.find(l) == uf.find(r):
                st = True
            res.append(st)
        
        return res