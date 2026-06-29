class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        # skip
        # buy 
        
        @cache
        def dp(i , h):

            if i == len(prices):
                return 0

            res = dp(i + 1 , h)
            if h:
                res = max(res , prices[i] + dp(i + 1 , False) )
            else:
                res = max(res , -prices[i] - fee + dp(i + 1 , True))
            
            return res
        

        return dp(0 , False)