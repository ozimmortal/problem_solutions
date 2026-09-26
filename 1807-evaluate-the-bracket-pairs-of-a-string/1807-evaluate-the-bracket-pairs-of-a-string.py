class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        coll = {}
        for key , val in knowledge:
            coll[key] = val
        
        i = 0
        res = ""
        while i < len(s):
            if s[i] == "(":
                i += 1
                key = ""
                while i < len(s) and s[i] != ")":
                    key += s[i]
                    i += 1
                res += coll[key] if key in coll else "?"
            else:
                res += s[i]
            
            i += 1
        
        return res
