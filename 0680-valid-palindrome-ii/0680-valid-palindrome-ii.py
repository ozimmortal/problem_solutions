class Solution:
    def validPalindrome(self, s: str) -> bool:
        st ,en = 0 , len(s) -1
        r = 0

        def ispalindrome(st, en):
            while st < en:
                if s[st] != s[en]:
                    return False
                st += 1
                en -= 1
            return True

        while st < en:
            
            if s[st] != s[en]:
                return ispalindrome(st , en -1) or ispalindrome(st + 1, en)

            st += 1
            en -= 1
        
        return True

