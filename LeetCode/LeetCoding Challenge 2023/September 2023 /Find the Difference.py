
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if len(s) == 0:
            return t[0] 
        for i in t:
            if s.count(i) != t.count(i):
                return i
              
