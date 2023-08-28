
def f(i,j,arr,dp):
    if(i==0 and j==0):
        return arr[0][0]
    if(i<0 or j<0):
        return sys.maxsize
    if dp[i][j] != -1:
        return dp[i][j]
    
    up = arr[i][j] + f(i-1,j,arr,dp)
    left = arr[i][j] + f(i,j-1,arr,dp)
    
    dp[i][j] = min(up,left)
    return dp[i][j]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for x in range(m)]
        
        return f(m-1,n-1,grid,dp)
        
