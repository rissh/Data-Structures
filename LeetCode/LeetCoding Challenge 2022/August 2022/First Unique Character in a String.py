
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for num in s:
            if s.count(num) == 1:
                return s.index(num)
        return -1
      
