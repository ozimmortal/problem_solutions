class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
        n = len(s)
        cnt = s.count("1")

        i = 0
        zeros = []
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i+=1
            
            if s[start] == "0":
                zeros.append(i - start)
        
        m = len(zeros)
        if m < 2: return cnt

        sur = 0
        for i in range(m - 1):
            sur = max(sur , zeros[i] + zeros[i + 1])

        return sur + cnt 



                

                
            