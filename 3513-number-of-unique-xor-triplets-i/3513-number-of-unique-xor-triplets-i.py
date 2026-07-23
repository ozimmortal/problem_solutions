class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2: return n
        
        b = int(log(n , 2)) + 1
        return 2 ** b