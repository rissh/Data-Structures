
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        
        n = len(bottomLeft)
        m = len(topRight)
        res = 0
        
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                x2 = min(topRight[i][0], topRight[j][0])
                y2 = min(topRight[i][1], topRight[j][1])

                if x1 < x2 and y1 < y2:
                    side = min(x2 - x1, y2 - y1)
                    res = max(res, side * side)
                
                j += 1
            i += 1
        
        return res
      
