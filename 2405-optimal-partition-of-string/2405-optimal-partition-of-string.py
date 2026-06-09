class Solution:
    def partitionString(self, s: str) -> int:
        
        seen = set()
        partition = 1

        left = 0 
        for right in range(len(s)):
            ch = s[right]

            if ch not in seen:
                seen.add(ch)
            else:
                partition += 1
                while left < right:
                    seen.remove(s[left])
                    left += 1
                seen.add(ch)

        return partition 
                



