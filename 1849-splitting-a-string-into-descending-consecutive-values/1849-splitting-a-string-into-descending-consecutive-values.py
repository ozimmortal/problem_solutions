class Solution:
    def splitString(self, s: str) -> bool:
        
        def solve(i , comb):

            if i == len(s):
                for j in range(1 , len(comb)):
                    if comb[j-1] - comb[j] != 1:
                        return False
                return len(comb) >= 2 
            

            for j in range(i , len(s)):
                v = int(s[i : j + 1])
                comb.append(v)
                if solve(j + 1 , comb):
                    return True
                comb.pop()
            return False

        return solve(0 , [])
