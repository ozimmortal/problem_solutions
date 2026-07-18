class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        
        MOD = 10 ** 9 + 7
        def to_base_x(n , base):
            num = []
            while n:
                n , rm = divmod(n , base)
                num.append(rm)
            return num[::-1]

        l , r = to_base_x(int(l) - 1 , b) ,to_base_x(int(r) , b)

        def solve(digits):
            @cache
            def dp(i ,t ,last):
                if i == len(digits): return 1
                
                limit = digits[i] + 1 if t else b
                cnt = 0
                for digit in range(last, limit):
                    cnt = (cnt + dp(i + 1, t and (digit == limit -1), digit)) % MOD
                
                return cnt % MOD
            return dp(0 , True , 0)
        
        cnt_l , cnt_r = solve(l)  , solve(r) 
        return (cnt_r - cnt_l + MOD) % MOD
        
                
