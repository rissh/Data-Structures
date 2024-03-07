
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        
        n = len(grid)
        m = len(grid[0])
        res = 0
    
        for row in range(n):
            for col in range(1, m):
                grid[row][col] += grid[row][col - 1]
    
        colInd = 0
        while colInd < m:
            sum_ = 0
            rowInd = 0
            while rowInd < n:
                sum_ += grid[rowInd][colInd]
                if sum_ <= k:
                    res += 1
                rowInd += 1
            colInd += 1
    
        return res
      
