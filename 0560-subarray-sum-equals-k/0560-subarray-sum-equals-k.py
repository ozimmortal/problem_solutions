from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter  = defaultdict(int)
        counter[0] = 1
        c = a = 0

        for n in nums:
            c += n
            a += counter[c-k]
            counter[c] +=1
        return a
        