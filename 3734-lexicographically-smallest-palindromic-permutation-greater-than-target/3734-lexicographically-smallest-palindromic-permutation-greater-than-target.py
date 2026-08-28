class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        if n == 1: return s if s > target else ""
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        
        half = n // 2
        odd = ""
        for i in range(26):
            if cnt[i] %2 == 1:
                if odd != "": return ""
                odd = chr(i + ord('a'))
            cnt[i] //= 2
        
        def check(c):
            left_per = left.copy()
            left_per.append(c)
            for i in range(25, -1, -1):
                left_per.extend([chr(ord("a") + i)] * cnt[i])

            palindrome = left_per + [odd] + left_per[::-1]
            return "".join(palindrome) > target
        
        left = []
        for i in range(half):
            found = False
            for j in range(26):
                if cnt[j] > 0:
                    cnt[j] -= 1
                    if check(chr(j + ord('a'))):
                        left.append(chr(j + ord('a')))
                        found = True
                        break
                    cnt[j] += 1
            if not found: return ""
        right = left[::-1]
        return "".join(left) + odd + "".join(right)


        


                        

        

        