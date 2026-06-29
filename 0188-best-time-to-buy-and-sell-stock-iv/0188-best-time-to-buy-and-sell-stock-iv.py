class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @cache
        def dp(i , h  , r):
            
            if i == len(prices) or r == 0:
                return 0
            
            ans = dp(i+ 1 , h , r)
            if h:
                ans = max(ans , prices[i] + dp(i + 1 , False , r - 1))
            else:
                ans = max(ans , -prices[i] + dp(i + 1 , True , r))
            
            return ans
        
        return dp(0 , False , k)
