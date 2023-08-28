# Method 1 : TLE
def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        index = 0
        for i in range(len(t)):
            if s[index] == t[i]:
                index += 1
            if index == len(s): 
                return True
        return False
    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        ans = []
        
        for word in words:
            if isSubsequence(self,word,s) == True:
                ans.append(word)
                
        return len(ans)
      
# Method 2 : 
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        lookup = defaultdict(list)
        output = 0
        
        for ind,char in enumerate(s):
            lookup[char].append(ind)
            
        def bs(lst,ind):
            l,r = 0,len(lst)
            while l < r:
                mid = (l+r)//2
                if ind < lst[mid]:
                    r = mid
                else:
                    l = mid+1
            return l
        
        for word in words:
            prev = -1
            found = True
            for char in word:
                temp = bs(lookup[char],prev)
                if(temp == len(lookup[char])):
                    found = False
                    break
                else:
                    prev = lookup[char][temp]
            if found:
                output += 1
        return output
