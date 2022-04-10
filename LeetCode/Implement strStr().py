
#Using Find() Method
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        return haystack.find(needle)
      
#Using Index() Method
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1
        return haystack.index(needle)
      
