class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l , c, a, = 0,0,0
        for r in range(len(nums)):
            if nums[r] == 0:
                c += 1
            
            while c > 1:
                if nums[l] == 0:
                    c -=1
                l +=1
            a = max(a,r - l)
        return a

        