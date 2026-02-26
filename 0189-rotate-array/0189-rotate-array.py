class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print(n)
        if n == 1:
            return 
        
      
        # reverse 
        s , e = 0 , n - 1

        while s < e:
            nums[s] , nums[e] = nums[e] , nums[s]

            s += 1
            e -= 1

        # reverse  >= k

        s , e = (k % n) , n - 1 

        while s < e:
            nums[s] , nums[e] = nums[e] , nums[s]

            s += 1
            e -= 1
        
        # reverse <k

        s , e = 0 , (k % n) -1

        while s < e:
            nums[s] , nums[e] = nums[e] , nums[s]

            s += 1
            e -= 1
        
        

    
        