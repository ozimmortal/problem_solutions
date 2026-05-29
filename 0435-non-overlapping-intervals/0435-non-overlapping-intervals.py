class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        curr = intervals[0]
        removed = 0

        for x , y in intervals[1:]:
            if x < curr[1]:
                if y <= curr[1]:
                    curr = [x , y]
                removed += 1
            else:
                curr = [x , y]
        
        return removed