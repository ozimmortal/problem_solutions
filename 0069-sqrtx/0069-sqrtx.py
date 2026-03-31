class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l = math.log(x,2)
        c = 0.5 * l
        res = 2 ** c
        return math.ceil(res) if math.ceil(res) - res < 0.00000001  else int(res)
        
