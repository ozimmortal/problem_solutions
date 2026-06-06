class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.scores = nums
        self.k = k
        heapq.heapify(self.scores)

        if k <= len(nums):
            for _ in range(len(nums) - k):
                heapq.heappop(self.scores)

    def add(self, val: int) -> int:
        
        if len(self.scores) < self.k:
            heapq.heappush(self.scores , val)
        else:
            if self.scores[0] < val:
                heapq.heappop(self.scores)
                heapq.heappush(self.scores , val)

        return self.scores[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)