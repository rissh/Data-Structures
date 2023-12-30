
class Solution:
    def isPathCrossing(self, path: str) -> bool:

        n = len(path)
        visited = set()
        direction = {
            "N" : [0,1],
            "S" : [0,-1],
            "E" : [1,0],
            "W" : [-1,0]
        }
        x,y = 0,0

        for c in path:
            visited.add((x,y))
            dx,dy = direction[c]
            x,y = x + dx, y + dy

            if (x, y) in visited:
                return True
        
        return False

