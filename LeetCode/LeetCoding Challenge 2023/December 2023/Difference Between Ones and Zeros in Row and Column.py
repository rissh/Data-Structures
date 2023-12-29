
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)
        m = len(grid[0])

        rowOnce = [0] * n
        colOnce =[0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rowOnce[i] += 1
                    colOnce[j] += 1

        res = [[None] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                res[i][j] = rowOnce[i] + colOnce[j] - (n - rowOnce[i]) - (m - colOnce[j])

        return res  
