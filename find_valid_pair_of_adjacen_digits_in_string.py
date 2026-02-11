class Solution:
    def findValidPair(self, s: str) -> str:
        c = Counter(s)
        for i in range(len(s) -1):
            if int(s[i]) == c[s[i]] and int(s[i+1]) == c[s[i+1]] and s[i] != s[i+1]:
                return s[i] + s[i + 1]
                
        return ""