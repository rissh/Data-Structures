
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0:
            return False
        length = len(s1) 
        for i in range(len(s2)-length+1):
            if Counter(s2[i:i+length]) == Counter(s1): 
                return True 
        return False 
        
