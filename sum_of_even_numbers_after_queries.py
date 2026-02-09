class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        def even_sum(arr):
            total = 0
            for n in arr:
                if n % 2 == 0:
                    total += n
            return total
        first_even = even_sum(nums)
        for val, index in queries:
            before = nums[index]
            if before % 2 == 0:
                first_even -= before
            nums[index] += val
            after = nums[index]
            if after % 2 == 0:
                first_even += after
            ans.append(first_even)
        return ans

        