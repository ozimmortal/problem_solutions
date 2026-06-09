class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:

        res = []

        if finalSum % 2 != 0:
            return  res

        start = 2
        curr_sum = 0

        while curr_sum < finalSum:
            curr_sum += start
            res.append(start)
            start += 2
        
        if curr_sum == finalSum:
            return res
        else:
            res.pop(res.index(curr_sum - finalSum))
            return res
            
        
