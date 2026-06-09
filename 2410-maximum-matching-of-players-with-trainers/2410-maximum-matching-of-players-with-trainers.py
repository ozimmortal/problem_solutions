class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n , m = len(players) , len(trainers)
        players.sort()
        trainers.sort()

        p1 , p2 = 0 , 0
        matches = 0

        while p1 < n and p2 < m:

            if players[p1] <= trainers[p2]:
                matches += 1
                p1 += 1
            
            p2 += 1
        
        return matches
        