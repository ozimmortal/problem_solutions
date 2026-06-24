class Solution:
    def tribonacci(self, n: int) -> int:

        sequence = [0 , 1 , 1]
        for i in range(3 , n + 1):
            t = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
            sequence.append(t)
        
        return sequence[n]


        