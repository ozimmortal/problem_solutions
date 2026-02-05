from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hint = {"A":0,"B":0}
        c = Counter(secret)

        for i,ch in enumerate(guess):
            if secret[i] == ch:
                hint["A"] += 1
                c[ch] -= 1
            elif ch in c:
                hint["B"] += 1
                c[ch] -= 1

            if c[ch] == 0:
                del c[ch]

            
        print(dict(c))
        return str(hint["A"]) + "A" + str(hint["B"]) + "B"
        
