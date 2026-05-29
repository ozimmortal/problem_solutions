class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]
        for interval in intervals[1:]:
            x  , y = interval
            if x <= res[-1][1]:
                res[-1][1] = max(y , res[-1][1])
            else:
                res.append(interval)
        return res
        

