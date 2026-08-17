class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m , n = len(mat) , len(mat[0])
        smat = [[0] *n for _ in range(m)]
        
        def val(x , y):
            return 0 <= x < m and 0 <= y < n
        
        # first row only 
        for r in range(1):
            for c in range(n):
                #  collect and sort
                nums = [mat[r][c]]
                x , y = r , c
                while True:
                    x += 1
                    y += 1
                    if not val(x , y):
                        break
                    nums.append(mat[x][y])
                
                nums.sort()
                x ,y = r , c
                for nu in nums:
                    smat[x][y] = nu
                    x += 1
                    y += 1
        
        for r in range(1 , m - 1):
            for c in range(1):
                nums = [mat[r][c]]
                x , y = r , c
                while True:
                    x += 1
                    y += 1
                    if not val(x , y):
                        break
                    nums.append(mat[x][y])
                
                nums.sort()
                x ,y = r , c
                for nu in nums:
                    smat[x][y] = nu
                    x += 1
                    y += 1
        smat[m-1][0] = mat[m-1][0]
        return smat





        