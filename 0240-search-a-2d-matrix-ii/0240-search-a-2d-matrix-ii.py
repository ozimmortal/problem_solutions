class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m , n = len(matrix) , len(matrix[0])
        def binary_search(row):
            left , right = 0 , n - 1
            while left <= right:
                mid = (left + right) // 2

                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        res = False
        for row in range(m):
            res = res or binary_search(row)
        
        return res