
class Solution:
    def minimumSteps(self, s: str) -> int:
        
        n = len(s)
        zeros = s.count('0')
        curr = 0
        res = 0

        for index in range(n):
            if s[index] == '0':
                res += index - curr
                curr += 1

        return res
    