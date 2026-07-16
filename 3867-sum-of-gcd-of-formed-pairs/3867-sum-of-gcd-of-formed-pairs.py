class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        prefixGrid = []
        mx = 0
        for n in nums:
            mx = max(mx , n)
            prefixGrid.append(gcd(mx , n))
        
        prefixGrid.sort()

        ans = 0
        left , right = 0 , len(prefixGrid) - 1
        while left < right:
            ans += gcd(prefixGrid[left] , prefixGrid[right])
            left += 1
            right -= 1
        
        return ans