class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        if s1 == s2:
            return 0

        c = Counter(s1 + s2)

        if c["x"] %2 != 0 or c["y"] %2 != 0:
            return -1

        d = defaultdict(int)
        for a,b in zip(s1 , s2):
            if a == b:
                continue
            d[a + b] += 1 
        ans = (d["xy"] // 2 + 1 if d["xy"] % 2 else d["xy"]// 2 ) + (d["yx"] // 2 + 1 if d["yx"] % 2 else d["yx"]// 2 )
        return ans

        
        