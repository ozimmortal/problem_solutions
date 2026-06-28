class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo ={}
        def dp(i):
            if i in memo:
                return memo[i]

            if i >= len(questions):
                return 0
            point , skip = questions[i]

            memo[i] = max(dp(i + 1) , dp(i + skip + 1) + point)
            return memo[i]

        return dp(0)