class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        n = len(digits)
        res = set()
        
        for i in range(n):
            if digits[i] == 0: continue
            for j in range(n):
                if j == i: continue
                for k in range(n):
                    if k == j or k == i: continue
                    s = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if s % 2 == 0 and s not in res:
                        res.add(s)
        return len(res)
                        


        