from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        mc = Counter(magazine)

        result = True

        for r in rc:
            if r not in mc or rc[r] > mc[r]:
                result = False
        return result

        