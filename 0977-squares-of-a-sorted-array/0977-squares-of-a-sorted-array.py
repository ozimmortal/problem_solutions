class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = [ ]
        l , r = 0 , len(nums) - 1

        while l <= r:
            a , b = nums[l] ** 2 , nums[r] ** 2
            if a  >= b:
                res.append(a)
                l += 1
            else:
                res.append(b)
                r -= 1

        return res[::-1] 



        
        