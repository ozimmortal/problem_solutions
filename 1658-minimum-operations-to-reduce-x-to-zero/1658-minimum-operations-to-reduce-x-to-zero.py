class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        total = sum(nums)
        if total < x: return -1

        left ,curr = 0 , 0
        MAX_SIZE = -1

        for right in range(len(nums)):
            curr += nums[right]
            
            while curr > total - x:
                curr -= nums[left]
                left += 1
            
            if curr == total - x:
                MAX_SIZE = max(MAX_SIZE, right - left + 1)
        
        return len(nums) - MAX_SIZE if MAX_SIZE > -1 else -1
            
    