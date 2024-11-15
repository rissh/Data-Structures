
class Solution:
    def compressedString(self, word: str) -> str:
        
        n = len(word)
        comp = ""
        i = 0
        
        while i < n:

            char = word[i]
            res = 1
            while i + res < len(word) and word[i + res] == char and res < 9:
                res += 1

            comp += str(res) + char
        
            i += res
    
        return comp 
