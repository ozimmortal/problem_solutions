class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        arr = [0] * (max(trips , key= lambda x : x[2])[2] + 1)
        for pas , f , t in trips:
            arr[f] += pas
            arr[t] -= pas
        
        curr = 0
        for val in arr:
            curr += val
            if curr > capacity:
                return False
        
        return True

