class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        keys= sorted(counts , key = lambda x : counts[x])

        for key in keys:
            dedact = min(counts[key] , k)
            counts[key] -= dedact
            if counts[key] == 0:
                del counts[key]
            
            k -= dedact
            if k == 0:
                break
        return len(counts)
