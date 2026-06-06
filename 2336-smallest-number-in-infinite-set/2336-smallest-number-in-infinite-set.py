class SmallestInfiniteSet:

    def __init__(self):
        self.infiniteSet = [1]
        self.counter = 1
        heapq.heapify(self.infiniteSet)
        

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.infiniteSet)
        self.counter += 1
        if self.counter not in self.infiniteSet:
            heapq.heappush(self.infiniteSet , self.counter)
        return smallest
        

    def addBack(self, num: int) -> None:
        if num not in self.infiniteSet:
            heapq.heappush(self.infiniteSet , num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)