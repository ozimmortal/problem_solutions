class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n , MAX = len(piles) , max(piles)
        def check(k):
            t = 0
            for p in piles:
                t += ceil(p / k)
            return t <= h
        
        left , right = 1 , MAX
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
