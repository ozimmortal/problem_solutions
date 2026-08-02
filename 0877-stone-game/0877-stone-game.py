class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        even_s = 0
        for i in range(0 , len(piles) , 2):
            even_s += piles[i]
        odd_s = 0
        for j in range(1 , len(piles), 2):
            odd_s += piles[j]
        
        return  even_s != odd_s 
            

        
