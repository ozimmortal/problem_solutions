class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        count  = 0
        for i , c in enumerate(citations):
            if c >= i + 1 :
                count += 1
            else:
                break
        return count