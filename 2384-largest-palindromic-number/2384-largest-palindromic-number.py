class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        counts = Counter(num)
        keys = sorted(counts , reverse=True)
        res = ""

        for key in keys:
            freq = counts[key]

            if key == "0" and len(res) == 0:
                    continue
            
            if freq % 2 == 0:
                res += key * (freq // 2)
                del counts[key]
                
            elif freq % 2 != 0 and freq > 1:
                res += key * ((freq - 1) // 2)
                counts[key] = 1
        
        ch = ""
        if len(counts) > 0:
            ch = max(counts)
        
        return  res + ch + res[::-1]
            
            