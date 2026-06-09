class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        keys = sorted(counts , key= lambda x : counts[x] , reverse=True)
        n = len(arr)
        half = n / 2

        removed = 0
        for key in keys:
            count = counts[key]
            if (n - count) <= half :
                return removed + 1

            n -= count
            removed += 1
        
        return rmoved

