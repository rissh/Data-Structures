
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        
        
        if (sx == fx and sy == fy):
            if(t != 1):
                return True
            return False
        
        diff_x = abs(fx - sx)
        diff_y = abs(fy - sy)
        res = max(diff_x, diff_y)

        if res <= t:
            return True
        
        else:
            return False
          
