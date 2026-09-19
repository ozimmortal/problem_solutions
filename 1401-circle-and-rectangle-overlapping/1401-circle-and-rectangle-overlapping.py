class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        # line x = x1
        if radius ** 2 - (x1 - xCenter) ** 2 >= 0:
            y = sqrt(radius ** 2 - (x1 - xCenter) ** 2) + yCenter
            if y1 <= y <= y2 : return True
        # line x = x2
        if radius ** 2 - (x2 - xCenter) ** 2 >= 0:
            y = sqrt(radius ** 2 - (x2 - xCenter) ** 2) + yCenter
            if y1 <= y <= y2: return True
        # line y = y1
        if radius ** 2 - (y1 - yCenter) ** 2 >= 0:
            x = sqrt(radius ** 2 - (y1 - yCenter) ** 2) + xCenter
            if x1 <= x <= x2: return True
        # line y = y2
        if radius ** 2 - (y2 - yCenter) ** 2 >= 0:
            x = sqrt(radius ** 2 - (y2 - yCenter) ** 2)  + xCenter
            if x1 <= x <= x2: return True
        
        #circle inside rectangle
        if x1 <= xCenter < x2 and y1 <= xCenter <= y2:
            return True
        # rectangle inside circle
        if sqrt((x2 -xCenter) ** 2 + (y2 - yCenter)**2) <= radius:
            return True

        return False
        
