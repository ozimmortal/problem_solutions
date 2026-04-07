class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:  

        def check(div):
            t = 0
            for n in nums:
                t += math.ceil(n / div)
            return t <= threshold

        left = 1
        right = max(nums)

        while left <= right:
            div = (left + right) // 2

            if check(div):
                right = div - 1
            else:
                left = div + 1
        return left
        