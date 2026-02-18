from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i] = str(n)
             
        return str(int("".join(sorted(nums,key= lambda n : n *10 ,reverse=True))))
