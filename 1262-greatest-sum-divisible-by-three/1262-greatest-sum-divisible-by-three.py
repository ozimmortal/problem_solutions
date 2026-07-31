class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        total , sm_one , sm_two = 0 , float('inf') , float('inf')
        for n in nums:
            total += n
            if n % 3 == 1:
                sm_two = min(sm_two , n + sm_one)
                sm_one = min(sm_one , n)
            
            if n %3 == 2:
                sm_one = min(sm_one , n + sm_two)
                sm_two = min(sm_two , n)
        
        if total % 3 == 0:
            return total
        
        if total % 3 == 1:
            return total - sm_one
        
        if total % 3 == 2:
            return total - sm_two
        
        return 0
        
