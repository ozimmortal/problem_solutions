class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        weight.sort()

        carry , amount = 5000 , 0
        for w in weight:
            if carry - w < 0:
                break
            amount += 1
            carry -= w
            
        return amount