class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return nums
        
        p1 = 0
        for p2 in range(len(nums)):

            if nums[p2] != 0 :
                nums[p1] , nums[p2] = nums[p2] , nums[p1]
                p1 += 1
            


        