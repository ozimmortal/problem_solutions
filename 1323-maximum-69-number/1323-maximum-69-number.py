class Solution:
    def maximum69Number (self, num: int) -> int:
        
        ans = [n for n in str(num)]
        idx = str(num).find("6")

        if idx != -1:
            ans[idx] = "9"
        
        return int("".join(ans))

        