class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        ans = 0
        coll = defaultdict(list)
        for r , s in reservedSeats:
            coll[r].append(s)
        
        for r in coll:
            seats = [False] * 10
            for s in coll[r]:
                seats[s - 1] = True
            start = 1
            while start <  6:
                can_be = True
                for i in range(start , start + 4):
                    if seats[i]:
                        can_be = False
                        break
                if can_be:
                    start += 4
                    ans += 1
                else:
                    start += 2
        rest = n - len(coll)

        return ans + rest * 2 