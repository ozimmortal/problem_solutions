class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def check(t):
            trips = 0
            for i in time:
                trips += t // i
            return trips >= totalTrips

        left , right = min(time), min(time) * totalTrips
        while left <= right:
            t = (left + right) // 2
            if check(t):
                right = t - 1
            else:
                left = t + 1
        return left
            