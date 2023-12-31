
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        n = len(s)
        hashMap = {}
        res = -1

        for i,c in enumerate(s):
            if c in hashMap:
                res = max(res, i - hashMap[c] - 1)
            else:
                hashMap[c] = i

        return res
      
