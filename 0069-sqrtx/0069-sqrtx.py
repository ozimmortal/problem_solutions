class Solution:
    def mySqrt(self, x: int) -> int:
        # if x == 0 or x == 1:
        #     return x
        # l = math.log(x,2)
        # c = 0.5 * l
        # res = 2 ** c
        # return math.ceil(res) if math.ceil(res) - res < 0.00000001  else int(res)

        l = 0
        r = x
        ans = 0

        while l <= r:

            m = (l + r) // 2

            if m * m == x:
                ans = m
                break
            elif m * m  > x:
                r = m -1
            else:
                ans = m
                l = m + 1
        return ans
        
