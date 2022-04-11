
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M,N = len(grid),len(grid[0])
        
        def posTotal(r,c):
            return r*N+c
        def valTopos(v):
            return [v//N, v%N]
        
        res = [[0]*N for i in range(M)]
        
        for r in range(M):
            for c in range(N):
                newVal = (posTotal(r,c)+k) % (M*N)
                newR, newC = valTopos(newVal)
                res[newR][newC] = grid[r][c]
        return res
      
