class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for ch in s:
            if ch.isalpha() :
                new_s += ch.lower()

        ptr1 , ptr2 = 0 , len(new_s) - 1

        if len(new_s) == 1:
            print(new_s)
            return False

        while ptr1 < ptr2:
            if new_s[ptr1] != new_s[ptr2]:
                return False
            ptr1 +=1
            ptr2 -= 1
        return True
        