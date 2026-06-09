class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        b = 0

        l , r = 0  , len(people) - 1

        while l <= r:
            s = people[l] + people[r]
            if s <= limit:
                l += 1
            b += 1    
            r -= 1
        
        return b
