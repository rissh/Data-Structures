
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n = len(word1)
        m = len(word2)
        
        if(n==0 and m>0):
            return m
        
        prev = [0 for i in range(m+1)]
        cur = [0 for i in range(m+1)]
        
        for j in range(m+1):
            prev[j] = j
            
        for i in range(1,n+1):
            cur[0] = i
            for j in range(1,m+1):
                if(word1[i-1] == word2[j-1]):
                    cur[j] = prev[j-1]
                else:
                    cur[j] = 1 + min(prev[j-1],prev[j],cur[j-1])
            prev = [x for x in cur]        
        return cur[m]
        
