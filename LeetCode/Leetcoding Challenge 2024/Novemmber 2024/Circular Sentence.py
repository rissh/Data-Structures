
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        n = len(sentence)
        
        if(sentence[0] != sentence[n-1]):
            return False
        
        for i in range(n):
            if(sentence[i] == " " and sentence[i-1] != sentence[i+1]):
                return False
            
        return True    
        
        
