
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def find_pattern(num):
            res = []
            hashmap = defaultdict(int)
            i = 0
            for x in num:
                if x in hashmap:
                    res.append(hashmap[x])
                else:
                    i+=1
                    hashmap[x]=i
                    res.append(hashmap[x])
            return res
        
        ans = []
        p = find_pattern(pattern)
        for word in words:
            if(find_pattern(word) == p):
                ans.append(word)
        return ans
      
