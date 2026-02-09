class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num % 3 != 0 :
            return []
        else:
            b = num//3
            return [b -1 , b,b +1]