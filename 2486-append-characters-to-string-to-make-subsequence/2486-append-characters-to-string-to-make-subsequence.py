class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m , n = len(s) , len(t)
        p1 , p2 = 0 , 0

        while p1 < m and p2 < n:
            if s[p1]  == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1

        return n - p2


        