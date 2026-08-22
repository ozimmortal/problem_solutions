class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        su , mul = 0 , 1
        t = n
        while t > 0:
            d = t % 10
            su += d
            mul *= d
            t //=10
        t = (su + mul)
        print(t , su , mul)
        return n % (su + mul) == 0