class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def check(c1 ,c2):
            for k in c1:
                if c1[k] > c2[k]:
                    return False
            return True
        
        if len(t) > len(s): return ""

        t, curr = Counter(t) , Counter()
        left , res = 0 , s
        flag = False
        

        for right in range(len(s)):
            curr[s[right]] += 1

            while check(t , curr):

                if right - left + 1 <= len(res):
                    res = s[left : right + 1]
                flag = True
                
                curr[s[left]] -= 1

                if curr[s[left]] == 0:
                    del curr[s[left]]
                
                left += 1
        
        

        return res if flag else ""




         