class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lib = {
            "2" : "abc",
            "3" : "def",
            "4" :"ghi",
            "5" : "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9" : "wxyz" 
        }
        ans = []
        
        def backtrack(curr , i):
            if len(curr) == len(digits):
                ans.append("".join(curr))
                return

            p = lib[digits[i]]
            for d in p:
                curr.append(d)
                backtrack(curr , i + 1)
                curr.pop()
        backtrack([] , 0)
        return ans
            
