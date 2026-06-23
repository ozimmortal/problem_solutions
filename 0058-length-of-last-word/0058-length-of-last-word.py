class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip()
        return len(s[::-1].split(" " ,1)[0])