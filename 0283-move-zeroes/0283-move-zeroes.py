class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        for r in range(len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r] , nums[l]
            
            while nums[l] != 0 and l < r:
                l += 1

        
            


        