class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int: 
        
        ans =0
        for l in range(len(nums)):
            cnt_target = 0
            for r in range(l , len(nums)):
                if nums[r] == target:
                    cnt_target += 1
                
                length = r - l + 1
                if cnt_target > (length) / 2:
                    ans += 1
            
        return ans

                
        