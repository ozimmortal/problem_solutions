class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0 : return 0

        queue = deque([(coin , 1) for coin in coins])
        seen = set(coins)
        while queue:

            total , n = queue.popleft()
            
            if total == amount:
                return n

            for coin in coins:
                t = total + coin 
                if t <= amount and t not in seen:
                    seen.add(t)
                    queue.append((t , n + 1))
        return -1