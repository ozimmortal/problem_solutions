class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        ans = []
        n = len(nums)    
        for i in range(n - 3):
            for j in range(i + 1,  n):
                l , r = j + 1 , n - 1
                while l < r:
                    arr = [nums[i], nums[j], nums[l], nums[r]]
                    s = sum(arr)
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        if arr not in ans:
                            ans.append(arr)
                        l += 1
                        
                

        
        return ans
        
        