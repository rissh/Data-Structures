class Solution:
    def minChanges(self, s: str) -> int:
        
        n = len(s)
        index = 0
        changes = 0
        
        while index < n - 1:
            
            if s[index] != s[index + 1]:
                changes += 1
                
            index += 2
            
        return changes
