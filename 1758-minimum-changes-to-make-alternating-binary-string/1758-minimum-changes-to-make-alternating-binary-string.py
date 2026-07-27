class Solution:
    def minOperations(self, s: str) -> int:
        
        
        n = len(s)
        if n < 2: return 0

        poss = []
        if n%2 == 0:
            k = n // 2
            poss.append("01" * k)
            poss.append("10" * k)
        else:
            k = n // 2
            poss.append("01" * k + "0")
            poss.append("10" * k + "1")
        def diff(s , p):
            d = 0
            for i in range(len(s)):
                d += 1 if s[i] != p[i] else 0
            return d
        
        ans = float('inf')
        for p in poss:
            ans = min(ans , diff(s , p))
        
        return ans

        