
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        prev = [-1] * 256
        
        i = 0
        for j in range(n):
            i = max(i,prev[ord(s[j])]+1)
            maxend = j-i+1
            res = max(res,maxend)
            prev[ord(s[j])] = j
            
        return res 
      
