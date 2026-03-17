class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        c = defaultdict(list)
        res = []
        for i , g in enumerate(groupSizes):
            c[g].append(i)
        
        for k,v in c.items():
            n = len(v)
            for i in range(0 , n , k):
                res.append(v[i:i + k])

        return res
        