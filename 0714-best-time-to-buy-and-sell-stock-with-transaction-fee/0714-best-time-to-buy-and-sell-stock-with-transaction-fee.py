class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        # skip
        # buy 
        
        memo = {}
        def dp(i , h):

            if i == len(prices):
                return 0
            if (i , h) in memo:
                return memo[(i , h)]
                
            res = dp(i + 1 , h)
            if h:
                res = max(res , prices[i] + dp(i + 1 , False) )
            else:
                res = max(res , -prices[i] - fee + dp(i + 1 , True))
            
            memo[(i , h)] = res
            return memo[(i, h)]
        

        return dp(0 , False)