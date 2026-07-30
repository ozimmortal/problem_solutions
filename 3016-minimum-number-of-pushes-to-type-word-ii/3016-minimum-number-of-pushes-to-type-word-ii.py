class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        
        freq.sort(reverse=True)
        total = 0
        start = 8
        for f in freq:
            if f:
                total += ((start) // 8) * f
                start +=1
        return total