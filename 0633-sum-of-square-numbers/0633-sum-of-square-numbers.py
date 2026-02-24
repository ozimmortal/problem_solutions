class Solution:
    def judgeSquareSum(self, c: int) -> bool:        
        l ,r = 0 ,(c // 2) + 1

        while l <= r:
            b = l ** 2 + r **2
            if b == c:
                return True
            elif b > c:
                r -=1
            else:
                l +=1
        return False


