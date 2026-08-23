class Solution:
    def sumGame(self, num: str) -> bool:
        
        n = len(num)
        h = n // 2

        aq , at = 0 , 0
        for i in range(h):
            if num[i] == "?":
                aq += 1
            else:
                at += int(num[i])
        
        bq , bt = 0 , 0
        for i in range(h , n):
            if num[i] == "?":
                bq += 1
            else:
                bt += int(num[i])
        
        if (bq + aq) %2 == 1: return True
        d = (at - bt)
        f = (bq - aq) // 2 * 9
        print(d , f)
        return d != f
