class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = 0
        temp = points[0]

        for i in range(1,len(points)):
            # check for intersection 

            if points[i][0] <=  temp[1]:  
                #  this means they intersect 
                # if they intersect update the temp variable
                temp = [points[i][0] , min(temp[1],points[i][1])]
            else:
                # if they dont intersect
                n += 1
                temp = points[i]

        return n + 1


        