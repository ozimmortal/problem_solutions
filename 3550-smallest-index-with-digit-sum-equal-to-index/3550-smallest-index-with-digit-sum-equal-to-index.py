class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        def digit_sum(n):
            res = 0
            while n > 0:
                res += n % 10
                n //=10
            return res
        
        for i in range(len(nums)):
            if i == digit_sum(nums[i]):
                return i
        return -1