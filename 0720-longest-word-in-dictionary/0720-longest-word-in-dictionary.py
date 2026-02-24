class Solution:
    def longestWord(self, words: List[str]) -> str:
        check = set()

        words.sort()

        ans = ""
        print(words)
        for w in words:
            nw = ""
            n = len(w)
            for i,ch in enumerate(w):
                nw += ch
                if nw not in check:
                    # to add to check and update ans 
                    #  1. i need to check if it is at the end of string 
                    #  2. that is only when i can update
                    if i == n - 1:
                        check.add(nw)
                        if len(ans) < len(w):
                            ans = w 
                        elif len(ans) == len(w):
                            ans =min(ans,w)
                    break         
        return ans

        

