class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        total = sum(nums)

        while k:
            small = heapq.heappop(nums)
            total -= small

            small *= -1
            total += small
            heapq.heappush(nums , small)
            k -= 1

        return total
