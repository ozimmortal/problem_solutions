class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # curr = 0
        # for i in range(k):
        #     curr += nums[i]
        # ans = curr / k
        # for j in range(k,len(nums)):
        #     curr += nums[j] - nums[j - k]
        #     ans = max(ans,curr/k)
            
        # return ans

        curr , ans = 0 , float('-inf')
        l = 0

        for r in range(len(nums)):
            curr += nums[r]

            if r - l + 1 == k:
                ans = max(ans,curr / k)
                curr -= nums[l]
                l += 1
                
        return ans


            
        