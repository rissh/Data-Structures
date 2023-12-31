
class Solution:
    def maximumLength(self, s: str) -> int:
        
        res = 0
        hashMap = [[] for _ in range(26)]

        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            hashMap[ord(s[i]) - ord('a')].append(j - i)
            i = j

        for counts in hashMap:
            if not counts:
                continue
                
            n = len(counts)
            counts.sort()
            
            res = max(res, counts[n - 1] - 2)
            if n > 1:
                res = max(res, min(counts[n - 1] - 1, counts[n - 2]))
            if n > 2:
                res = max(res, counts[n - 3])

        return res if res != 0 else -1
      
