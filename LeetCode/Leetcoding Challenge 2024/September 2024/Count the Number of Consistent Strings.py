
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        res = len(words)

        for word in words:
            for char in word:
                if char not in allowed:
                    res -= 1
                    break
                    
        return res
      
