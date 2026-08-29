class UF:
    def __init__(self , nums, limit):
        self.parent = { x:x for x in nums}
        self.limit = limit
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self , x , y):
        rx , ry = self.find(x) , self.find(y)
        if abs(x - y) <= self.limit:
            self.parent[ry] = rx
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        uf = UF(nums, limit)
        s = sorted(nums)

        for i in range(1 , len(s)):
            uf.union(s[i] , s[i - 1])
        
        comp = defaultdict(SortedList)
        res = [0] * len(s)
        for i , x in enumerate(nums):
            c = uf.find(x)
            res[i] = c
            comp[c].add(x)
        
        for i , c in enumerate(res):
            res[i] = comp[c].pop(0)
        
        return res



       
        