class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        rem = 0
        res = ""

        p1 , p2 = len(a) -1 , len(b) - 1
        while p1 > -1 and p2 > -1:
            ch1 , ch2 = a[p1] , b[p2]
            t = int(ch1) + int(ch2) + rem
            if t <= 1:
                res += str(t)
                rem = 0
            else:
                rem = 1
                res += "0" if t == 2 else "1"
            p1 -= 1
            p2 -= 1
        
        while p1 > -1:
            t = int(a[p1]) + rem
            if t <= 1:
                res += str(t)
                rem = 0
            else:
                rem = 1
                res += "0" if t == 2 else "1"
            p1 -=1
        
        while p2 > -1:
            t = int(b[p2]) + rem
            if t <= 1:
                res += str(t)
                rem = 0
            else:
                rem = 1
                res += "0" if t == 2 else "1"
            p2 -=1

        if rem:
            res += "1"
        return res[::-1]

