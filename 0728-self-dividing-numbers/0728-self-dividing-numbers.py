class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def self_div(n):
            t = n
            while t > 0:
                d = t % 10
                if d == 0 or n % d != 0:
                    return False
                t //= 10
            return True
        
        nums = []
        for i in range(left, right + 1):
            if self_div(i):
                nums.append(i)
        
        return nums