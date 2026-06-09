class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : (x[1] , x[0]) , reverse=True)
        
        unit = 0
        i = 0 
        while truckSize and i < len(boxTypes):
            boxes , unit_per_box = boxTypes[i]
            min_boxes = min(truckSize , boxes)
            unit += min_boxes * unit_per_box

            i += 1
            truckSize -= min_boxes
        return unit

        