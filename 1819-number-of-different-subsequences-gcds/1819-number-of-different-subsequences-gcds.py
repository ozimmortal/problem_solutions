class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        
        m = max(nums)
        nums = set(nums)
        ans = 0

        for i in range(1 , m + 1):
            curr = 0
            for j in range(i , m + 1 , i):
                if j in nums:
                    curr = gcd(curr , j)
            
                    if i == curr:
                        ans += 1
                        break

        return ans
