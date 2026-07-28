class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        
        num = 0
        div = [0] * len(word)
        for i , ch in enumerate(word):
            num = ((num * 10) + int(ch)) % m
            if num == 0:
                div[i] = 1
        return div