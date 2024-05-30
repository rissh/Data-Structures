
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        n = len(queries)
        BallColour = {}
        ClourCount = {}
        distinct = set()
        res = []
        
        for ball, color in queries:
            
            if ball in BallColour:
                prev_color = BallColour[ball]
                ClourCount[prev_color] -= 1
                
                if ClourCount[prev_color] == 0:
                    distinct.remove(prev_color)
            
            BallColour[ball] = color
            ClourCount[color] = ClourCount.get(color, 0) + 1
            distinct.add(color)
            
            res.append(len(distinct))
        
        return res
