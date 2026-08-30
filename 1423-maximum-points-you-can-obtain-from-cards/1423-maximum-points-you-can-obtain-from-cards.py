class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)
        total = sum(cardPoints)
        j = n - k
        t =  sum(cardPoints[0:j])
        ans = total - t
        
        for i in range(j, n):
            l = i - j
            t = t - cardPoints[l] + cardPoints[i]
            ans = max(ans , total - t )
        
        return ans
