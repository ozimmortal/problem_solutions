class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        left , cnt = 0 , 0
        ans = ''

        for right in range(len(s)):
            cnt +=  int(s[right])
            while cnt == k:
                d , w = (right - left + 1) , s[left: right + 1]
                if ans == '' or len(ans) > d:
                    ans = w
                elif len(ans) == d:
                    ans = min(ans , w)
                
                cnt -= int(s[left])
                left += 1
        return ans
