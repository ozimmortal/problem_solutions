class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        ans = ""
        for w in dictionary:
            ptr1 , ptr2 = 0 , 0
            while ptr1 < len(w) and ptr2 < len(s):
                if w[ptr1] == s[ptr2]:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    ptr2 += 1
            
            if ptr1 == len(w):
                if len(ans) < len(w):
                    ans = w 
                elif len(ans) == len(w):
                    ans =min(ans,w)
        
        return ans
        

        

        