class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]

        f , s = nums[0] , max(nums[0] , nums[1])
        for i in range(2, len(nums)):
            curr = f + nums[i]
            f , s = s , max(curr , s)
        
        return s

            
        