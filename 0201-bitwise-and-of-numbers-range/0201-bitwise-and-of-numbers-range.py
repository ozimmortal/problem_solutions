class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        

        cnt, diff , pref = 0 , right - left , 0
        res = 0
        while left:
            sb = left & 1
            if sb:
                pref |= 1 << cnt
                if diff < (1 << (cnt+ 1)) - pref:
                    res |= 1 << cnt
            cnt += 1
            left >>= 1
        
        return res
        
                
        