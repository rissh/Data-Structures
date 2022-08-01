
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prev = [0] * n
        for i in range(0,m):
            curr = [0] * n
            for j in range(0,n):
                
                if(i==0 and j==0):
                    curr[j] = 1
                    
                else:
                    up,left = 0,0
                    
                    if(i>0):
                        up = prev[j]
                    if(j>0):
                        
                        left = curr[j-1]
                    curr[j] = up+left
                    
            prev = [x for x in curr]        
                    
        return prev[n-1]
        
        
