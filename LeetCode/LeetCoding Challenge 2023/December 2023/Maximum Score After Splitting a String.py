
class Solution:
    def maxScore(self, s: str) -> int:

        n = len(s)
        zeros = 0
        once = s.count("1")
        res = 0

        for i in range(n - 1):
            if s[i] == "0":
                zeros += 1
            else:
                once -= 1

            res = max(res, zeros + once)

        return res
      
