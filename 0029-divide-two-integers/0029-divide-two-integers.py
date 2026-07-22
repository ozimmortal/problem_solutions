class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        NEGATIVE_LIMIT = -2**31
        POSITIVE_LIMIT = 2**31 - 1

        if NEGATIVE_LIMIT == dividend and divisor == -1: return POSITIVE_LIMIT

        negative = (dividend < 0) != (divisor < 0)
        a , b = abs(dividend) , abs(divisor)
        res = 0

        while a >= b:
            temp = b
            mul = 1
            while a >= (temp << 1):
                temp <<=1
                mul <<= 1
            a -= temp
            res += mul

        return - res if negative else res 




