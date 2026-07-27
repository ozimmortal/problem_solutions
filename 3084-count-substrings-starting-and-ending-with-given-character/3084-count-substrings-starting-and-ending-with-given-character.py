class Solution:
    def countSubstrings(self, s: str, c: str) -> int:

        cnt = s.count(c)

        def rs(n):
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 3
            return n + rs(n - 1)
        
        return rs(cnt)
