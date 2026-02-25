class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        pc = Counter(p)
        sc = defaultdict(int)
        k = len(p)
        l = 0
        
        if len(s) < k:
            return ans
        for  i in range(k):
            sc[s[i]] += 1
        
        if pc == sc:
            ans.append(0)
        for r in range(k,len(s)):
            
            print(sc)
            sc[s[l]] -= 1
            if sc[s[l]] <= 0:
                del sc[s[l]]
            l += 1
            sc[s[r]] += 1
            if pc == sc:
                ans.append(l)
        return ans
           