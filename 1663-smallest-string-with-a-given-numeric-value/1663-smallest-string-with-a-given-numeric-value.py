class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        s = ["a"] * n
        i = n - 1
        k -= n

        while i >=0 and k:
            if k - 26 >= 0:
                s[i] = chr(ord("a") + 25)
                k -= 25
            else:
                s[i] = chr(ord("a") + k)
                k = 0
            
            i -= 1

        return "".join(s)

