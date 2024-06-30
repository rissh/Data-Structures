
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        
        MiniRow, MiniCol = float('inf'), float('inf')
        MaxiRow, MaxiCol = float('-inf'), float('-inf')

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    MiniRow = min(MiniRow, r)
                    MaxiRow = max(MaxiRow, r)
                    MiniCol = min(MiniCol, c)
                    MaxiCol = max(MaxiCol, c)

        height = MaxiRow - MiniRow + 1
        width = MaxiCol - MiniCol + 1

        area = height * width

        return area
