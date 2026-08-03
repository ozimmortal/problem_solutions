class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        t = sum(stoneValue)
        n = len(stoneValue)

        @cache
        def dp(turn , i):
            if i == n:
                return 0
            
            total = 0
            res = float('-inf') if turn else float('inf')
            for x in range(1 , 4):
                if i + x > n: break
                total += stoneValue[i + x - 1]
                if turn:
                    res = max(res , total + dp(not turn, i + x))
                else:
                    res = min(res , dp(not turn, i + x))
            
            return res
        
        alice = dp(True, 0)
        bob = t - alice
        
        print(alice)
        if alice > bob:
            return "Alice"
        elif alice < bob:
            return "Bob"
        
        return "Tie"