class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        ans = 0
        while a or b or c:
            d = (a | b) & 1
            lc = c & 1
            if d != lc:
                ans += (a & 1) + (b & 1) if lc == 0 and d == 1 else 1
            c >>= 1
            b >>= 1
            a >>= 1
        return ans

        

                

        
        

            