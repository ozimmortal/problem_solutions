class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n , m = len(matrix) , len(matrix[0])

        left , right = 0 , n * m - 1

        while left <= right:

            mid = (left + right) // 2

            num = matrix[mid//m][mid%m]

            if num == target:
                return True
            
            if num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False