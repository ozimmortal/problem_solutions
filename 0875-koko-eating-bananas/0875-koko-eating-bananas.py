class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            t = 0 
            for p in piles:
                t += math.ceil(p / k)
            return t <= h
        
        left = 1
        right = max(piles)
        ans = float('inf')
        while left <= right:
            k= (left + right) // 2
            if check(k):
                ans = min(ans , k)
                right = k - 1
            else:
                left = k + 1
        return ans 
