class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l  = 1 
        n = len(nums)
        for r in range(1 , n):
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        
        return l

        