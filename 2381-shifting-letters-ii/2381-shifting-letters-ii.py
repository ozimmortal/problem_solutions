class Solution:
   
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        diff = [0] * (len(s) + 1)
        for l , r , k in shifts:
            if k :
                diff[l] += 1
                diff[r + 1] -= 1
            else:
                diff[l ] -= 1
                diff[r + 1] += 1

        prefix = [diff[0]]
        for i in range(1,len(s)):
            prefix.append(prefix[i -1] + diff[i])
        
        res = ""
        for i , ch in enumerate(s):
            asc = ord(ch) % 97 + prefix[i] % 26
            res += chr(asc%26 + 97)
        return res
            