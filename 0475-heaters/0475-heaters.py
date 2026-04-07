class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def check(rad):
            i = 0 
            for house in houses:

                while i < len(heaters) and heaters[i] + rad < house:
                    i += 1
                if i == len(heaters) or heaters[i] - rad > house:
                    return False

            return True

        left = 0
        right = max(houses) + min(heaters)

        while left <= right:
            rad = (left + right )// 2

            if check(rad):
                right = rad - 1
            else:
                left = rad + 1
        
        return left
        
        