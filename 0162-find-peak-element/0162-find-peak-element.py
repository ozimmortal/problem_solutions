class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def check_valid(x):
            if x == 0  and nums[x + 1] < nums[x]:
                return True
            elif x == n - 1 and nums[x - 1] < nums[x]:
                return True
            elif 0 < x < n -1  and nums[x - 1] < nums[x] > nums[x + 1]:
                return True
            return False

        n = len(nums)
        if n == 1: return 0

        left , right = 0 , len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if  check_valid(mid):
                return mid
            elif mid + 1 < n and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1 
            