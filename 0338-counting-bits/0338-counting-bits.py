class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0 , 1 , 1 , 2]
        if n < 4: return dp[:n + 1]

        offset = 4
        for i in range(4 , n + 1):
            if offset * 2 == i:
                offset *= 2
            dp.append(1 + dp[i - offset])

        return dp
        