
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        n = len(colors)
        res = 0
        i = 0
        
        while i < n:
            if colors[i] != colors[(i + 1) % n] and colors[(i + 1) % n] != colors[(i + 2) % n]:
                res += 1
            i += 1
        
        return res
        
