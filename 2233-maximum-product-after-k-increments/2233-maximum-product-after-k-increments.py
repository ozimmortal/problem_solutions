class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        heapq.heapify(nums)

        while k:
            x = heapq.heappop(nums)
            heapq.heappush(nums , x + 1)
            k -= 1
        
        mul = 1
        for num in nums:
            mul = (mul * num) % MOD
        return mul % MOD
