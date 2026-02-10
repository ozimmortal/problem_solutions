class Solution:
    def isHappy(self, n: int) -> bool:
        
        def s(num):
            total = 0
            n = num
            while n > 0:
                r = n % 10
                if r == 0:
                    n = n//10
                total += r ** 2
                n -= r
               
            return total
        tracker = set()

        while n not in tracker:
            tracker.add(n)
            n = s(n)
            
            if n == 1:
                return True
            
        return False
