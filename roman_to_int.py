class Solution:
    def romanToInt(self, s: str) -> int:
        V = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        num = V[s[-1]]

        for i in range(len(s) - 1,0,-1):

            if V[s[i ]]  <= V[s[ i - 1]]:
                num += V[s[i-1]]
            else:
                num -= V[s[i - 1]]
        return num
        