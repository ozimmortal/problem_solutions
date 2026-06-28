class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def dp(p1 , p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0
            
            cnt = 0

            if text1[p1] == text2[p2]:
                cnt += dp(p1+1 , p2 + 1) + 1
            else:
                cnt += max(dp(p1 + 1 , p2) , dp(p1 , p2 + 1))
            
            return cnt

        return dp(0 , 0)