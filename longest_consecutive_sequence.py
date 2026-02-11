class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        c = set(nums)
        ans = 0
        for n in c:
            if n - 1 not in c:
                length = 0
                temp = n
                while temp in c:
                    length += 1
                    temp += 1
                ans = max(ans,length)

        return ans