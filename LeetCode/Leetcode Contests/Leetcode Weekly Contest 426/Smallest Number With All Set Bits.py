
class Solution:
    def smallestNumber(self, n: int) -> int:
        
        res = 1  
        while res < n:
            res = res * 2 + 1  
            
        return res

