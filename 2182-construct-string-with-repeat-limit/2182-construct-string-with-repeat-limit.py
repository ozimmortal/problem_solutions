class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        counts = Counter(s)
        heap = []
        for ch , freq in counts.items():
            heapq.heappush(heap , -ord(ch))
            

        res = ""
        while heap:
            ch = chr(-heapq.heappop(heap))
            freq = counts[ch]
            mul = min(freq , repeatLimit)

            res += ch * mul
            counts[ch] -= mul

            if counts[ch] !=0 and heap:
                ch2 = chr(-heapq.heappop(heap))
                res += ch2
                counts[ch2] -= 1

                if counts[ch2] != 0:
                    heapq.heappush(heap , -ord(ch2))
                heapq.heappush(heap , -ord(ch))
        
        return res


