class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        new_nums = []
        seen = set()

        for n in nums:
            if n not in seen:
                new_nums.append(n)
                seen.add(n)
        left = 0
        right = len(new_nums) - 1
        ans = float('inf')
        while  left <= right:
            mid = (left + right) // 2
            ans = min(ans , new_nums[mid])
            if new_nums[mid] > new_nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
 