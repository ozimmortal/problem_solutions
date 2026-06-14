class Solution:
    def reverse(self, x: int) -> int:
        
        negative = True if x < 0 else False
        x = abs(x)
        digits = 1
        temp = x

        while temp > 9:
            digits *= 10
            temp //= 10
        print(digits)
        ans = 0
        while x > 0:
            rm = x % 10
            ans += rm * digits
            digits //= 10
            x //= 10
        if ans >= (-2 ** 31) and ans <= (2**31) -1 :
            return - ans if negative else ans
        return 0 
