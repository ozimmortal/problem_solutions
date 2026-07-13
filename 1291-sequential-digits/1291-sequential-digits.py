class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        seq = []
        for i in range(1 , 9):
            curr = i
            while curr <= high:
                t = (curr % 10) + 1
                if t == 10:
                    break
                curr = (curr * 10) + (t)
                if low <= curr <= high:
                    seq.append(curr)

        return sorted(seq)            



