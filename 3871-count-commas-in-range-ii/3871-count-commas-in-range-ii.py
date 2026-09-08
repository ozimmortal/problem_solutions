class Solution:
    def countCommas(self, n: int) -> int:
        
        def dig(n):
            res = 0
            while n >= 10:
                n //= 10
                res += 1
            return res

        d = dig(n)
        cnt = d // 3
        ans = (n - (10 ** d )) * (cnt) + cnt
        while d > 3:
            top = (10 ** d) - 1
            d -= 1
            cnt = d // 3
            ans += (top - (10 ** d )) * (cnt) + cnt
        
        return ans

