class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:

        def perm(r):
            acc = 1
            for f in freq:
                if not f: continue
                if f > r: return 0
                acc *= comb(r , f)
                if acc > k: return acc
                r -= f
            return acc

        n = len(s)
        half = n // 2
        freq = [0] * 26
        for i in range(half):
            freq[ord(s[i]) - ord('a')] += 1
        
        left = []
        start = 0
        for i in range(half):
            selected = False
            for chi in range(26):
                if not freq[chi] : continue
                freq[chi] -= 1

                p = perm(half - i - 1)
                if start + p >= k:
                    left.append(chr(chi + ord('a')))
                    selected = True
                    break
                
                freq[chi] += 1
                start += p
            
            if not selected: return ""
        
        mid = "" if n %2 == 0 else s[half]
        return "".join(left) + mid + "".join(left[::-1])



        
        
        