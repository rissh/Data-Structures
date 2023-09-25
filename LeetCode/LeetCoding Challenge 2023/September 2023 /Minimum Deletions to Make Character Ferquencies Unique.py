
class Solution:
    def minDeletions(self, s: str) -> int:
        
        cnt = collections.Counter(s)
        res = 0
        used = set()
        
        for char, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res  
