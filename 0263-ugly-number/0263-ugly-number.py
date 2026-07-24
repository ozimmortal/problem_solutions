class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n<=0: return False
        while n > 1:
            if n %2 != 0 and n %3 != 0 and n%5 != 0:
                return False

            for k in [2 ,3 , 5]:
                if n %k == 0:
                    n //=k
        
        return True

        