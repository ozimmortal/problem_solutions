class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()

        last = points[0]
        res = 0

        for i in range(1 , len(points)):
            if points[i][0] <= last[1]:
                last[1] = min(last[1], points[i][1])
            else:
                res += 1
                last = points[i]
        
        return res + 1
