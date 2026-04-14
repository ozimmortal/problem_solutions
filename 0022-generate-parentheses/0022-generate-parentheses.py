class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def valid(s):
            b = []
            for c in s:
                if b and b[-1] == "(" and c == ")":
                    b.pop()
                    continue
                b.append(c)
            return len(b) == 0
        
        def backtrack(path):
            
            if len(path) == n *2:
                if valid(path):
                    res.add("".join(path))
                return

            
            for b in ['(' , ')']:
                path.append(b)
                backtrack(path)
                path.pop()
                
        

        res = set()
        backtrack([])
        return list(res)
        