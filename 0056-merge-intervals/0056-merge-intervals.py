class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        last = intervals[0]

        for i in range(1 , len(intervals)):
            ls , le = last
            s , e = intervals [i]

            if s <= le:
                last = [min(ls , s) , max(le , e)]
                continue
            res.append(last)
            last = intervals[i]
        
        res.append(last)
        return res

