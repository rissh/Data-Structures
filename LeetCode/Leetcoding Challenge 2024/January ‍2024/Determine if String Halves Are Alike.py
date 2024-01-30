

def f(num):
    
    if(num == 'a' or num == 'e' or num == 'i' or num == 'o' or num == 'u' or num == 'A' or num == 'E' or num == 'I' or num == 'O' or num == 'U'):
        return True
    
    return False

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        count1 = 0
        count2 = 0
        
        for i in range(n//2):
            if(f(s[i])):
                count1 += 1
        
        for i in range(n//2,n):
            if(f(s[i])):
                count2 += 1
                
        return count1 == count2        
