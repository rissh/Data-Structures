
class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        n =len(word)
        res = 1
        for i in range(n - 1):

            if word[i] == word[i + 1]:
                res += 1
                
        return res
      
