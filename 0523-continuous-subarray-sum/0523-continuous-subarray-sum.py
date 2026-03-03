class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        counter = {0:-1}
        total = 0
        for i , n in enumerate(nums):
            total += n
            r = total % k
            if r not in counter:
                counter[r] = i
            elif i - counter[r] > 1 :
                return True
            
        return False
            
