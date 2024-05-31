
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        n = len(s)

        currCost = 0
        left = 0 
        res = 0

        for right in range(n):
            currCost += abs(ord(s[right]) - ord(t[right]))

            while currCost > maxCost:

                currCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            res = max(res, right - left + 1)

        return res
      
