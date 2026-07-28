class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # if len(s) == 1:
        #     return s
        c = Counter(s)
        ns = sorted(list(c.keys()))
        lp = ""
        for ch in ns :
            lp += ch * (c[ch] // 2)
            c[ch] -= (c[ch] // 2) * 2

            if c[ch] == 0:
                del c[ch]
        rp = lp[::-1]
        md = ""
        for k in c :
            md = k
        return lp + md + rp