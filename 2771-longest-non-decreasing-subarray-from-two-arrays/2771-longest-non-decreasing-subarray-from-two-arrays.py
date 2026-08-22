class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        dp1 , dp2 = 1 , 1
        ans = 1

        for  i in range(1 , n):

            la , lb = nums1[i - 1] , nums2[i - 1]
            a , b = nums1[i] , nums2[i]
            ndp1 , ndp2 = 1 , 1

            if a >= la:
                ndp1 = max(ndp1 , dp1 + 1)
            if a >= lb:
                ndp1 = max(ndp1 , dp2 + 1)

            if b >= la:
                ndp2 = max(ndp2 , dp1 + 1)
            if b >= lb:
                ndp2 = max(ndp2 , dp2 + 1)
            
            dp1 , dp2 = ndp1 , ndp2
            ans = max(ans , dp1 , dp2)
        
        return ans


