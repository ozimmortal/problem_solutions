class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverseArr(i , j):
            while i < j:
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
                j -= 1
            
        n = len(nums)
        rot = k % n
        if rot == 0: return 

        reverseArr(0 , n- 1)
        reverseArr(rot , n - 1)
        reverseArr(0 , rot - 1)

       
        
        

    
        