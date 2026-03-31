class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       
        res = [-1 , -1]
        n = len(nums)
        # find left 

        l = 0
        r = n - 1

        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] == target:
                res[0] = mid
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1

        if res[0] == -1:
            return res
        
        l = res[0]
        r = n - 1
        print(l , r)
        while l <= r:
            mid = (l + r) // 2
           
            if nums[mid] == target:
                res[1] = mid
                l = mid + 1
            elif target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
        return res




                

