
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        rs, rt = '', ''
        
        for i in s:
            if i == '#':
                rs = rs[:-1]
            else:
                rs += i
        
        for i in t:
            if i == '#':
                rt = rt[:-1]
            else:
                rt += i
        
        return rs == rt
      
