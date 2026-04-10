class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        start = [ x for x, _ in flowers]
        end = [y for _ , y in flowers]

        start.sort()
        end.sort()

        res = []
        for t in people:
            start_idx = bisect_right(start , t)
            end_idx = bisect_left(end , t)
            res.append(start_idx - end_idx)
        
        return res


        