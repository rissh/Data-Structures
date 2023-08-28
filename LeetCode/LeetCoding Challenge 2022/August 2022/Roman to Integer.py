
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = d[s[0]]
        for i in range(1,len(s)):
            prev_val = d[s[i-1]]
            val = d[s[i]]
            if val>prev_val:
                res+=val-2*prev_val
            else:
                res+=val
        return res
      
