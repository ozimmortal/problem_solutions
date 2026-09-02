class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        even_cnt, odd_cnt = 0 , 0
        for i in range(n):
            if nums1[i] % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        
        # all odd
        all_odd = True
        for i in range(n):
            if nums1[i] % 2 == 0:
                if not odd_cnt:
                    all_odd = False
                    break
        
        all_even = True
        for i in range(n):
            if nums1[i] % 2 == 1:
                if not odd_cnt:
                    all_even = False
                    break
        
        return True if all_even or all_odd else False

