class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1] - x[0])
        
        n = len(intervals)
        ans = n

        for i in range(n):
            prevLeft  , prevRight = intervals[i]
            for j in range(i + 1 , n):
                currLeft , currRight = intervals[j]
                if currLeft <= prevLeft and prevRight <= currRight:
                    ans -= 1
                    break
            

        print(intervals)
        return ans
                 