class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        valid = ['a' , 'b' , 'c']

        def backtrack(curr,s):

            if len(curr) == n:
                res.append(curr[:])
                return
            
            for i in range(s, 3):
                le = valid[i]
                if not curr or curr[-1] != le:
                    curr.append(le)
                    backtrack(curr , s)
                    curr.pop()
        
        res = []
        backtrack([] , 0)
        return "" if len(res) < k else "".join(res[k -1])



