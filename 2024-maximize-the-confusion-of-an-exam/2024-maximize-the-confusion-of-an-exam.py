class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        res = 0
        # for false
        l ,curr = 0 , 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                curr += 1

            while curr > k:
                curr -= 1 if answerKey[l] == 'T' else 0
                l +=1

            res = max(res , r - l + 1)
        
        l ,curr = 0 , 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'F':
                curr += 1

            while curr > k:
                curr -= 1 if answerKey[l] == 'F' else 0
                l +=1

            res = max(res , r - l + 1)
        
        return res
         