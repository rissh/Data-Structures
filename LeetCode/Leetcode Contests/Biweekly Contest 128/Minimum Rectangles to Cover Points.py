class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        
        n = len(points)
        points.sort(key=lambda x: x[0])
        rectangles = 0
        current_end = float('-inf')
    
        for x, y in points:
            
            if x > current_end:
                
                rectangles += 1
                current_end = x + w
    
        return rectangles
        
