from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1_co,w2_co = Counter(word1),Counter(word2)

        if sorted(w1_co.keys()) == sorted(w2_co.keys()) and sorted(w1_co.values()) == sorted(w2_co.values()):
            return True
        return False