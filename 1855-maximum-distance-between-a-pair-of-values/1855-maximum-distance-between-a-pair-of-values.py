class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        res = 0
        nums2 = nums2[::-1]
        for i , n in enumerate(nums1):
            
            ri = bisect_left(nums2, n)
            j = len(nums2) - ri - 1
            res = max(res, j - i)
        return res
