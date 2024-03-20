
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        
        n = len(s)
        subs = set()
        
        for i in range(n - 1):
            subs.add(s[i:i+2])
            
        for sub in subs:
            if sub in s[::-1]:
                return True
        return False
        
