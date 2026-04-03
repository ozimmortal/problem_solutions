class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(arr , i):
            left = 0
            right = len(arr) -1

            while left <= right:
                mid = (left + right) // 2
                print(left , right , mid)
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return False

        for i ,row in enumerate(matrix) :
            if search(row,i):
                return True
        return False
