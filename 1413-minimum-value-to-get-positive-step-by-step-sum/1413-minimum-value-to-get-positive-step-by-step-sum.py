class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1] + nums[i])
            
        minPrefix = min(prefix)
        if minPrefix < 1:
            return abs(min(prefix)) + 1
        else:
            return 1
       