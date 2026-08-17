class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        sat = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                sat += customers[i]
        
        cons, mcons = 0 , 0 
        for i in range(minutes):
            if grumpy[i]:
                cons += customers[i]
        mcons = max(mcons , cons)
        for i in range(minutes, len(customers)):
            if grumpy[i - minutes]:
                cons -= customers[i - minutes]

            if grumpy[i]:  
                cons += customers[i]

            mcons = max(mcons , cons)

        return sat + mcons         
            
            
        