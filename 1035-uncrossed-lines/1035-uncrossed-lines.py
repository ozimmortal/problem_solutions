class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(i , j):
            if i == m:
                return 0

            res = dp(i + 1 , j)
            for k in range(j , n):
                if nums1[i] == nums2[k]:
                    res = max(res , 1 + dp(i + 1 , k + 1))
            
            return res
        m , n = len(nums1) , len(nums2)
        
        return dp(0 , 0)
            