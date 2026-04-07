class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def check(speed):
            time = 0
            for d in dist[:-1]:
                time += math.ceil(d/speed)
            time += dist[-1] / speed
            return time <= hour
        
        left = 1
        right = 10**7

        if not check(right):
            return -1
        
        while left <= right:
            speed = (left + right) // 2
            if check(speed):
                right = speed - 1
            else:
                left = speed + 1
        return left