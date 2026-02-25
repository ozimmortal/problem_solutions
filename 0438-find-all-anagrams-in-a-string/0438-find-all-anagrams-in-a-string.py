class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        pc = Counter(p)
        k = len(p)
        
        for i in range(len(s) - k + 1):
            dc = Counter(s[i:i+k])

            if pc == dc:
                ans.append(i)
        return ans
           