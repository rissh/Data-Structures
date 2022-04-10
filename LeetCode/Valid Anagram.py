
# Using Hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        countS,countT = {},{}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
            
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            
        return True
      
# Using Counter()
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)
      
# Using Sort() Function
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        S = list(s)
        T = list(t)
        
        S.sort()
        T.sort()
        
        if T==S:
            return True
        else:
            return False
          
#Using Sorted() Function
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)
         
