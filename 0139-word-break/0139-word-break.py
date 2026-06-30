class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dp(i , j):

            if i < len(s) and j >= len(wordDict):
                return False 

            if i >= len(s):
                return True
            
            res = False
            if s[i:].startswith(wordDict[j]):
                n = len(wordDict[j])
                res = res or dp(i+n , 0) or dp(i , j + 1)
            else:
                res = res or dp(i, j + 1)

            return res
        
        return dp(0 , 0)


            