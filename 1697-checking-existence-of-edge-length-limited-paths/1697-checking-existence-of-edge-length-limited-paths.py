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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        edgeList.sort(key = lambda x :x[2])
        
        q = [(l , s ,e ,i)  for i , (s , e , l) in enumerate(queries)]
        q.sort()

        uf = UF(n)

        size = len(edgeList)
        res = [False] * len(queries)
        idx = 0
        for l ,s ,e , i in q:
            while idx < size and edgeList[idx][2] < l:
                uf.union(edgeList[idx][0] , edgeList[idx][1])
                idx += 1
            
            res[i] = uf.find(s) == uf.find(e)
        
        return res


