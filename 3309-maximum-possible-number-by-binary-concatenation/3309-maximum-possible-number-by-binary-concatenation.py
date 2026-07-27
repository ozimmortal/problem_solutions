class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        
        ans = 0
        for p in permutations(nums):
            temp = 0
            for num in p:
                k = floor(log(num , 2)) + 1
                temp = max(temp , (temp << k ) + num)
            ans = max(ans , temp)
        
        return ans
        