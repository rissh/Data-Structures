
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
        n = len(hours)
        res = 0
        hashMap = {}
        
        for n in hours:
            mod = n % 24
            complement = (24 - mod) % 24
        
            res += hashMap.get(complement, 0)
        
            hashMap[mod] = hashMap.get(mod, 0) + 1
    
        return res
        
