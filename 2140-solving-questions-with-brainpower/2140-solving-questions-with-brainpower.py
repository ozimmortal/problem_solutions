class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            point , skip = questions[i]

            return max(dp(i + 1) , dp(i + skip + 1) + point)

        return dp(0)