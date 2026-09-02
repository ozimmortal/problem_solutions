class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        odd = float('inf')
        for i in range(n):
            if nums1[i] % 2 == 1:
                odd= min(odd , nums1[i])
        
        print(odd)
        # all odd, odd + even = odd
        all_odd = True
        for i in range(n):
            if nums1[i] % 2 == 0 and odd >= nums1[i]:
                all_odd = False
                break

        # all even, odd + odd = even
        all_even = True
        for i in range(n):
            if nums1[i] % 2 == 1 and odd >= nums1[i]:
                all_even = False
                break

        return True if all_even or all_odd else False