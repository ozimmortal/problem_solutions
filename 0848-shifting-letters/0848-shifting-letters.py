class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        
        prefix = [shifts[-1]]
        for i in range(len(s) -1):
            prefix.append(prefix[i] + shifts[len(s) - 2 -i])

        res = ""
        for i , ch in enumerate(s):
            asc = ord(ch) % 97 + prefix[len(s) - i - 1] % 26
            res += chr(asc%26 + 97)
        return res