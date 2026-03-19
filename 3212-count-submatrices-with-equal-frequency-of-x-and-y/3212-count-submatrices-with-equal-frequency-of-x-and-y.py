class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n , m = len(grid) , len(grid[0])
        prefix = [[0] * (m + 1) for _ in range(n + 1)]
        seen_x = []
        for i in range(1,n+1):
            for j in range(1 , m+1):
                b = 0
                if grid[i-1][j-1] == "X":
                    b = 1
                    seen_x.append([i-1,j-1])
                elif grid[i-1][j-1] == "Y":
                    b = -1

                prefix[i][j] = prefix[i - 1][j] + prefix[i][j -1] + b -prefix[i-1][j-1]
        res = 0
        
        for i in range(1,n+1):
            for j in range(1 , m+1):
                if prefix[i][j] == 0 and seen_x:
                    for x in seen_x:
                        if x[0] <=  i -1 and x[1] <= j- 1:
                            res +=1
                            break
        return res
