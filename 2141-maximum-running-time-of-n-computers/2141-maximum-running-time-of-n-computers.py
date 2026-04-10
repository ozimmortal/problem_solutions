class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def check(m):
            t = 0
            for b in batteries:
                t += min(b , m)
            return t >= m * n

        l , r = min(batteries) , sum(batteries) // n  
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid -1
        return ans