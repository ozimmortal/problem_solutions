class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1
        for r in range(1 ,n):
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l
        
        

        