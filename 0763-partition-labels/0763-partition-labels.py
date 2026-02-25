class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        res = []
        c = defaultdict(int)
        n = len(s)

        for i ,ch in enumerate(s[::-1]):
            if ch not in c:
                c[ch] = n - i -1
        si , e = 0 , 0
        for i , ch in enumerate(s):
            si += 1
            e = max(e,c[ch])

            if e == i:
                res.append(si)
                si = 0
        
        return res

        