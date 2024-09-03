
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        
        n = len(s)
        res = ""
        
        for i in range(0, n, k):
            
            nums = s[i:i+k]
            
            sums = sum(ord(char) - ord('a') for char in nums)
            hashChar = chr((sums % 26) + ord('a'))
            
            res += hashChar
            
        return res
      
