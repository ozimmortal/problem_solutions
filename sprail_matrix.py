class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n , m = len(matrix) , len(matrix[0])
        output = []
        left , right , top ,bottom = 0 ,m , 0, n

        while left < right and top < bottom:

            # outwards

            for i in range(left,right):
                output.append(matrix[top][i])
            top += 1

            for i in range(top ,bottom):
                output.append(matrix[i][right - 1])
            right -= 1
            
            if left >= right or top >= bottom:
                break

            # inwards

            for i in range(right - 1 , left - 1 , -1):
                output.append(matrix[bottom -1][i])
            bottom -= 1

            for i in range(bottom-1 ,top -1 , -1):
                output.append(matrix[i][left])
            left += 1
        return output
        
        