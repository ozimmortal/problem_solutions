class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_max , gb_max = 0 , -inf
        for num in nums:
            curr_max = max(num , curr_max + num)
            gb_max = max(gb_max, curr_max)
        
        return gb_max



       
        