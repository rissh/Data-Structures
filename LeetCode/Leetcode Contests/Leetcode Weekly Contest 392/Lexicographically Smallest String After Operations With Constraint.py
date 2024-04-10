
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        
        n = len(s)
        s = list(s)
        
        for i in range(n):
            for j in range(26):
                
                new = chr(ord('a') + j)
                cyclic_dist = min(abs(ord(s[i]) - ord(new)), 26 - abs(ord(s[i]) - ord(new)))
                
                if cyclic_dist <= k:
                    s[i] = new
                    k -= cyclic_dist
                    break
                    
        return ''.join(s)
        
