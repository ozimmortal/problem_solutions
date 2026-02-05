from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsC = Counter(chars)
        ans = 0
        for s in words:
            if len(s) > len(chars):
                continue
            sC = Counter(s)
            f = 1
            for k in sC:
                if k not in charsC or charsC[k] < sC[k]:
                    f = 0
            if f:
                ans += len(s)
        return ans
        