class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        pairs = set()
        for i in range(n):
            for j in range(i , n):
                pairs.add( nums[i] ^ nums[j])
        
        unq = set()
        for num in nums:
            for t in pairs:
                unq.add(num ^ t)
        
        return len(unq)
    