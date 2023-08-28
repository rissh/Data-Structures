
class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'(': ')', '{':'}', '[':']'}
        opening = []
        closing = []
    
        for element in s:
        
            if element in dict1:
                opening.append(element)
            
            else:
                closing.append(element)
            
                if len(opening)>0 and len(closing)>0:
                    start = opening[len(opening)-1]
                    end = closing[len(closing)-1]
                    if dict1[start] == end:
                        opening.pop()
                        closing.pop()
                
        if len(opening) == 0 and len(closing) == 0:
            return True
            
