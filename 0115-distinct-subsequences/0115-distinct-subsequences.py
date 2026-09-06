class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        if len(s) < len(t): return 0
        if len(s) == len(t): return 1 if s == t else 0
        @cache
        def dp(i , j):
            
            if j == len(t):
                return 1

            if i == len(s):
                return 0 

            res = dp(i + 1 , j)
            if s[i] == t[j]:
                res += dp(i + 1 , j + 1)

            return res
        
        return dp(0 , 0)
        