class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dp(i , s):
            if i == len(coins) or s > amount:
                return 0

            if s == amount:
                return 1

            res = dp(i , s + coins[i]) + dp(i + 1 , s)
        
            return res

        return dp(0 , 0)