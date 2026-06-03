class MedianFinder:

    def __init__(self):
        self.smallHeap  , self.largeHeap = [] , []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap , -num)
        
        if len(self.smallHeap)  - 1 > len(self.largeHeap) or self.smallHeap and self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            val = - heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap , val)

        # if len(self.smallHeap)  - 1 > len(self.largeHeap):
        #     val = - heapq.heappop(self.smallHeap)
        #     heapq.heappush(self.largeHeap , val)

        if  len(self.largeHeap) -1 > len(self.smallHeap):
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap ,  -val)
            
            

    def findMedian(self) -> float:
        l1 , l2 = len(self.smallHeap) , len(self.largeHeap)
        if l1 > l2:
            return  - self.smallHeap[0]
        elif l1 < l2:
            return self.largeHeap[0]
        else:
            return (self.largeHeap[0] + ( - self.smallHeap[0])) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()