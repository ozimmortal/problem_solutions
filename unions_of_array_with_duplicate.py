class Solution:    
    def findUnion(self, a, b):
        # code here
        ans = set(a) | set(b)

        return list(ans)
        