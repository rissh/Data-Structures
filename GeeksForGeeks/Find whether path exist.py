
class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		#Code here
		stx = 0
        sty = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    stx = i
                    sty = j
                    break
        def solve(x,y):
            if x<0 or x>=n or y<0 or y>=n or grid[x][y]==0 or grid[x][y] ==-1:
                return False
            if grid[x][y] == 2:
                return True
            grid[x][y] = -1
            return solve(x+1,y) or solve(x-1,y) or solve(x,y+1) or solve(x,y-1)
        return solve(stx,sty)
        
