class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        smallest , largest = min(nums) , max(nums)
        res = []
        for i in range(smallest , largest + 1):
            if i not in nums:
                res.append(i)
        return res