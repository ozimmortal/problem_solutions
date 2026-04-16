class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        ans = float('inf')
        

        for a in range(len(nums) - 2):
            left , right  = a + 1 , len(nums) -1

            while left < right:
                t = nums[a] + nums[left] + nums[right]
                d = abs(t  -  target)
                if d < abs(ans  -  target):
                    ans = t

                if t > target:
                    right -= 1
                else:
                    left += 1
        return ans



            



            
            