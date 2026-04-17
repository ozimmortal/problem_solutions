class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        self.c = 0
        def backtrack(path , r):

            if len(path) == n:
                self.c += 1
                if self.c == k:
                    return "".join(path)
                return r
            
            for i in range(1 , n + 1):
                if r :
                    break
                if str(i) not in path:
                    path.append(str(i))
                    r = backtrack(path, r)
                    path.pop()
                
            return r
        
        return backtrack([],"")