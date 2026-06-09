class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        amount = 0
        for c in costs:
            if coins - c < 0:
                return amount
            amount += 1
            coins -= c
            
        return amount
        
