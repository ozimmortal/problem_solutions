class Item:
    def __init__(self , word , freq):
        self.word = word
        self.freq = freq

    def __lt__(self , to_compare):
        if self.freq == to_compare.freq:
            return self.word > to_compare.word

        return self.freq < to_compare.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        print(counts)
        heap = []
        for key , freq in counts.items():
            item = Item(key , freq)

            if len(heap) < k:
                heapq.heappush(heap , item)
            else:
                if heap[0] < item:
                    heapq.heappop(heap)
                    heapq.heappush(heap, item)


        
        res = []
        while heap:
            item = heapq.heappop(heap)
            res.append(item.word)
        
        return res[::-1]
                


        
        