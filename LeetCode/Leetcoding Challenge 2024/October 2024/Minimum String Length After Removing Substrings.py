
class Solution:
    def minLength(self, s: str) -> int:
        
        n = len(s)
        res = []
        ans = 0
        
        flag = True
        while flag:
            if "AB" in s:
                s = s.replace("AB", "", 1)
            elif "CD" in s:
                s = s.replace("CD", "", 1)
            else:
                flag = False
                
        ans = len(s)
        return ans

