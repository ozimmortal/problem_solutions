from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orc = Counter(s)
        result = ""
        for ch in order:
            if ch in orc:
                result += ch * orc[ch]
                del orc[ch]
        for r in orc:
            result += r * orc[r]
        return result