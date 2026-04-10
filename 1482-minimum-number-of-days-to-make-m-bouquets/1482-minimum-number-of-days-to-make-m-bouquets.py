class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def check(d):
            cf =0
            cm = 0
            for f in bloomDay:
                if f <= d:
                    cf += 1
                else:
                    if cf >= k:
                        cm += cf // k
                    cf = 0
            return cm + cf//k >= m
        l , r = 1 , max(bloomDay) 
        ans = -1
        while l <= r:
            d = (l + r) // 2
            if check(d):
                ans = d
                r = d -1
            else:
                l = d + 1
        return ans
