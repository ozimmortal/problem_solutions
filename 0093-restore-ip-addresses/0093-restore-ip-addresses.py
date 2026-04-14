class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def valid(a):
            if "".join(a) != s:
                return False
            for c in a:
               
                if int(c) > 255 or ( c[0] == "0" and len(c) > 1) :
                    return False
            return True

        def backtrack(path , st):
            if len(path) == 4:
                if valid(path):
                    res.append(".".join(path[:]))
                return

            for i in range(st , len(s)):
                path.append(s[st : i + 1])
                backtrack(path , i + 1)
                path.pop()
            

        res = []
        backtrack([] , 0)
        return res