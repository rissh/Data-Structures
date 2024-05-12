
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])
        
        ans = [[0] * (n-2) for i in range(n-2)]
        
        for p in range(n-2):
            for q in range(n-2):
                maxi = max(grid[p+1][q+1], grid[p+1 - 1][q+1], grid[p+1 + 1][q+1], grid[p+1][q+1 -1], grid[p+1][q+1 + 1],grid[p+1 - 1][q+1 -1], grid[p+1 + 1][q+1 + 1], grid[p+1 -1][q+1 +1], grid[p+1 + 1][q+1 - 1])
                ans[p][q] = maxi
                
        return ans        
