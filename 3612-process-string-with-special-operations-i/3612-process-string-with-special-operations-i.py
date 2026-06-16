class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for ch in s:

            if ch == "*":
                if res:
                    res.pop()
            elif ch == "#":
                dup = "".join(res)
                for ch in dup:
                    res.append(ch)
            elif ch == "%":
                res = res[::-1]
            else:
                res.append(ch)
        return "".join(res)