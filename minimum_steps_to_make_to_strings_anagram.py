class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c= Counter(s)
        steps = 0
        for ch in t:
            if ch in c:
                c[ch] -= 1
                if c[ch] == 0:
                    del c[ch]
            else:
                steps += 1
        return steps
