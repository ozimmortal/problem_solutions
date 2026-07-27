class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        l , validCount = 0 , 0
        ans = 0
        for r  in range(len(nums)):
            if nums[r] > right:
                l = r + 1
                validCount = 0
            elif nums[r] >= left:
                validCount = r - l + 1
            
            ans += validCount
        
        return ans
