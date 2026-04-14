class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        self.dic = set(wordDict)
        
        def backtrack(path , st):
           
            sen = " ".join(path[:])
            if path and len(sen) - (len(path) -1) == len(s):
                res.append(sen)
                return

            for i in range(st , len(s)):
                w = s[st: i+1]
                if w in self.dic:
                    path.append(w)
                    backtrack(path , i + 1)
                    path.pop()
        
        res = []
        backtrack([] , 0)
        return res