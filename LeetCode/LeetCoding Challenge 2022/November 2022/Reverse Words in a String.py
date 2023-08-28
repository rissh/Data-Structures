
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()
        return ' '.join(s[::-1])
    
    
    '''
    a=s.split()    
    a=a[::-1]
    return ' '.join(a)
    '''
    
