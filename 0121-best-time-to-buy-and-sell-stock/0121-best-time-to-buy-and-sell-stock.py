class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lmin = prices[0]
        res = 0

        for i in range(len(prices)):
            if prices[i] > lmin:
                res = max(res , prices[i] - lmin)
            
            lmin = min(lmin , prices[i])
        
        return res
        