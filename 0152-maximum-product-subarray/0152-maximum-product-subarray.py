class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        minSub , maxSub = 1 , 1
        for n in  nums:
            if n == 0:
                minSub , maxSub = 1 , 1
                continue
            
            t , k = n * minSub , n * maxSub
            minSub, maxSub = min(n  , t , k ) , max(n , t , k)
            res = max(res, maxSub)
        
        return res

            
        
        
