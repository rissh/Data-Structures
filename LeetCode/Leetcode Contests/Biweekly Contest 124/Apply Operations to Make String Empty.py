
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        
        n = len(s)
        hashMap = Counter(s)
        
        maxFreq = max(hashMap.values())
        res = ''
        
        i = n - 1
        while i >= 0:
            curr = s[i]
            
            if hashMap[curr] == maxFreq:
                hashMap[curr] = -1
                res = curr + res
            i -= 1
            
        return res
      
