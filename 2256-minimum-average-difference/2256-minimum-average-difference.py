class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        prefix =  [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])
        
        m , idx = float('inf') , 0

        for i in range(len(nums) - 1):
            ls = prefix[i] // (i + 1)
            rs = (prefix[-1] - prefix[i]) // (len(nums) - i - 1) 

            if abs(ls - rs) < m:
                m = abs(ls-rs)
                idx = i
        if prefix[len(nums)-1] // len(nums) < m:
            idx = len(nums) - 1
        
        return idx


        