class Solution:
    def minimumPushes(self, word: str) -> int:
        
        return sum(i // 8 for i in range(8 , 8 + len(word)))

