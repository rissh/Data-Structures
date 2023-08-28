
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wlen = len(words[0])  
        target_counter = Counter(words) 
        ret = [] 
        
        # Iterate over every index
        # e.g s="afoobar" we need to skip over "a"
        for l in range(len(s)-wlen+1):
            tokens = []
            
            # Try to read words of len(words[0])
            # If its not a match exit early
            for i in range(l, l+wlen*len(words), wlen):
                token = s[i:i+wlen]
                if token not in target_counter: break
                tokens.append(token)
            
            # Is the length of the words we could read the same as the target?
            # If so, check if the occurrences are the same
            if (len(tokens) == len(words) 
                and Counter(tokens)==target_counter):
                ret.append(l)
            
        return ret
      
