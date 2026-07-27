class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        freq = defaultdict(int)
        currSum = 0
        ans = 0
        for n in nums[:k]:
            freq[n] += 1
            currSum += n
        
        if len(freq) == k:
            ans = max(ans , currSum)
        l = 0
        for i in range(k , len(nums)):
            currSum += nums[i] - nums[l]
            freq[nums[i]] += 1
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0:
                del freq[nums[l]]
            l += 1

            if len(freq) == k:
                ans = max(ans , currSum)
        
        return ans
        
