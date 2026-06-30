class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @cache
        def dp(i, s):
            if i == n:
                return 1 if s == target else 0
            
            res = 0
            for j in range(1 , k + 1):
                if s + j <= target:
                    res += dp(i + 1 , s + j)
            
            return res
        
        return dp(0 , 0) % ((10**9) + 7)