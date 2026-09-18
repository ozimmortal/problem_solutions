class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        
        intervals = {}
        for i , c in enumerate(s):
            if c not in intervals:
                intervals[c] = [i , i]
            else:
                intervals[c][1] = i


        for c in intervals:
            while True:
                nl , nr = intervals[c]
                for i in range(nl , nr + 1):
                    nc = s[i]
                    intervals[c][0] = min(intervals[c][0] , intervals[nc][0])
                    intervals[c][1] = max(intervals[c][1] , intervals[nc][1])
                
                if nl  == intervals[c][0] and nr == intervals[c][1]:
                    break

        canidates = sorted(intervals.values() , key=lambda x : x[1])
        res = []
        prev = -1
        for start , end in canidates:
            if start > prev:
                res.append(s[start:end + 1])
                prev = end
        
        return res