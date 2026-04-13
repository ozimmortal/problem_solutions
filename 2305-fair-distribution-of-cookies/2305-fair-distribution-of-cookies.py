class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.res = float('inf')
        childs = [0] * k
        def backtrack(i):

            if  i == len(cookies):
                self.res = min(self.res , max(childs))
                return
            if max(childs) >= self.res:
                return 

            for j in range(k):
                childs[j] += cookies[i]
                backtrack(i + 1)
                childs[j] -= cookies[i]
        
        backtrack(0)
        return self.res

            