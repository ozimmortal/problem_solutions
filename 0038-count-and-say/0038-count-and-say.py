class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rle(s):
            count , before = 0 , s[0]
            res = ""
            for ch in s:
                if ch != before:
                    res += f"{count}{before}"
                    count = 0
                
                before = ch
                count += 1
            
            if before and count:
                res += f"{count}{before}"
            return res
        
        res = "1"
        while n - 1 > 0:
            res = rle(res)
            n -= 1

        return res    


