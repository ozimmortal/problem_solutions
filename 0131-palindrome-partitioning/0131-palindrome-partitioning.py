class Solution:
    def partition(self, s: str) -> List[List[str]]:

        
        def isit(w):
            l , r = 0 , len(w) - 1
            while l < r:
                if w[l] != w[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(path , st):

            if st == len(s):
                res.append(path[:])
                return
            
            for i in range(st , len(s)):
                w = s[st : i+1]
                if isit(w):
                    path.append(w)
                    backtrack(path , i + 1)
                    path.pop()
        
        res = []
        backtrack([] , 0)
        return res
                


        