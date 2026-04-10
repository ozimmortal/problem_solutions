class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        
        c = defaultdict(list)

        for l , h in rectangles:
            c[h].append(l)
        
        for k in c:
            c[k].sort()
        
        res = []
        for x , y in points:
            count = 0
            for i in range(y , 101):
                arr = c[i]
                idx = bisect_left(arr , x)
                count += len(arr) - idx
            res.append(count)
        return res
        

