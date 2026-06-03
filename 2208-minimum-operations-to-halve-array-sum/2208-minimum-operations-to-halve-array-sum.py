class Solution:
    def halveArray(self, nums: List[int]) -> int:
        

        heap = []
        for num in nums:
            heapq.heappush(heap , -num)

        step = 0
        initialSum = sum(nums)
        half = initialSum / 2
        while initialSum > half:
            num = abs(heapq.heappop(heap)) / 2
            initialSum -= num
            heapq.heappush(heap , -num)
            step += 1
        return step
            

        
        