class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k  =  0
        n = len(nums)
        needs_swap = False
        l , r = 0 , 1
        while l < r < n :
            if nums[l] == nums[r]:
                needs_swap = True
                k += 1
            elif nums[l] != nums[r]  and not needs_swap:
                l += 1

            if needs_swap and nums[l] != nums[r]:
                nums[l + 1] = nums[r]
                l += 1

            r += 1
        return n - k
        
        

        