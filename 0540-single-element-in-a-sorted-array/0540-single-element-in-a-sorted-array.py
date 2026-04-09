class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0 
        right = len(nums) - 1
        if len(nums) == 1: return nums[0]
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid -  1] != nums[mid] ) and ( nums[(mid + 1) % len(nums)] != nums[mid]):
                return nums[mid]
            elif (mid % 2 == 1 and nums[mid-1] != nums[mid]) or (mid % 2 == 0 and nums[mid-1] == nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        
            
        