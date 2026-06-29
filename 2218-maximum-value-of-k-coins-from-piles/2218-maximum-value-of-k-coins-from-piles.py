class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        @cache
        def dp(i , r):

            if i == len(piles) or r == 0:
                return 0
            
            res = dp(i + 1 , r)
            curr = 0
            for j in range(min(r , len(piles[i]))):
                curr += piles[i][j]
                res = max(res , curr + dp(i + 1 , r -  j - 1))

            return res
        
        
        return dp(0 , k)