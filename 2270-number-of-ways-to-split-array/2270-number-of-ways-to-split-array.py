class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i - 1] + nums[i])
        
        ans = 0

        for i in range(len(prefix) - 1):
            split_sum = prefix[-1] - prefix[i]
            if prefix[i] >= split_sum:
                ans += 1
        return ans 


        