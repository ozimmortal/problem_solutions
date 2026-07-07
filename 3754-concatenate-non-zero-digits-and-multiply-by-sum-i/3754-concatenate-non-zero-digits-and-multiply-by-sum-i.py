class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        mul= 1
        x = 0
        su = 0

        while n > 0:
            rem = n % 10
            if rem != 0:
                x += rem * mul
                mul *= 10
                
            su += rem
            n //= 10
        
        return su * x
