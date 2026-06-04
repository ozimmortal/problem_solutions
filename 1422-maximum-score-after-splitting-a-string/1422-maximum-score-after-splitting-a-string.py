class Solution:
    def maxScore(self, s: str) -> int:
       
        prefix = [1 if s[0] == "0" else 0]
        for i in range(1 ,len(s)):
            if s[i] == "0":
                prefix.append(prefix[i - 1] + 1)
            else:
                prefix.append(prefix[i - 1])

        suffix = [0] * len(s)
        suffix[-1] = 1 if s[-1] == "1" else 0 

        for i in range(len(s) - 2 , -1 , -1):
            if s[i] == "1":
                suffix[i] = suffix[i + 1] + 1
            else:
                suffix[i] = suffix[i  + 1]

        maxSum = 0
        for i in range(len(s)-1):
            maxSum = max(maxSum , prefix[i] + suffix[i + 1])
        
        return maxSum

        