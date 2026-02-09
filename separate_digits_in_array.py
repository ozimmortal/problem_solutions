class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n = "".join([str(x) for x in nums])
        return [int(i) for i in n]
        