class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        
        left , right = 1 , num
        
        while left <= right:
            mid = (left + right)// 2
            prod = mid * mid
            if prod == num:
                return True
            elif prod > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False