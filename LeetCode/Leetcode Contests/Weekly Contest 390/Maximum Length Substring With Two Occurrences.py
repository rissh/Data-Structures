
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        n = len(s)
        left = 0
        res = 0
        hashMap = Counter()
    
        for right, char in enumerate(s):
            hashMap[char] += 1
        
            while hashMap[char] > 2:
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]
                left += 1
        
            res = max(res, right - left + 1)

        return res
      
