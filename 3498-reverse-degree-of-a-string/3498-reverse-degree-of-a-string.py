class Solution:
    def reverseDegree(self, s: str) -> int:
        
        res = 0
        for i , ch in enumerate(s):
            res += (ord('z') - ord(ch) + 1) * (i + 1)
        return res
