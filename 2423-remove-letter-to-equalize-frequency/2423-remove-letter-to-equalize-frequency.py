class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        
        for ch in word:
            i = ord(ch) - ord('a')
            freq[i] -= 1
            c = set(f for f in freq if f!=0)
            if len(c) == 1: return True
            freq[i] += 1

        return False 