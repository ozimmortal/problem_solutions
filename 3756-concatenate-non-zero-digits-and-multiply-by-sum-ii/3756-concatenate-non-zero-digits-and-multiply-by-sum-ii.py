class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
    
        n = len(s)
        MOD = 10 ** 9 + 7
       
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i ] =( pow10[i - 1] * 10 )  % MOD
       
        prefix = [0]
        for i in range(len(s)):
            prefix.append(prefix[-1] + int(s[i]))
        
        x , cnt = [0] * (n+1) , [0] * (n+1)
        for i in range(n):
            num = int(s[i])
            x[i+1] =(x[i] * 10 + num) % MOD if num > 0 else x[i]
            cnt[i + 1] = cnt[i] +  (num > 0)
        
        res = []
        for l , r in queries:
            length = cnt[r + 1] - cnt[l]
            su = prefix[r + 1] - prefix[l]
            mul =( x[r + 1] - (x[l] * pow10[length])) % MOD
            res.append((mul * su) % MOD)
        return res
        