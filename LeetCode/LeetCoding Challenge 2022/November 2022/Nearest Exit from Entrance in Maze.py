
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        queue = deque([[entrance[0], entrance[1], 0]])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = set()
        visited.add(tuple(entrance))
        
        while queue:
            k = len(queue)
            
            for _ in range(k):
                x, y, steps = queue.popleft()
                
                for dx, dy in directions:
                    newX, newY = x+dx, y+dy
                    
                    if newX >= 0 and newX < m and newY >= 0 and newY < n and maze[newX][newY] == '.' and (newX, newY) not in visited:
                        if newX == 0 or newX == m-1 or newY == 0 or newY == n-1:
                            return steps + 1
                        visited.add((newX, newY))
                        queue.append([newX, newY, steps+1])
                        
        return -1
      
