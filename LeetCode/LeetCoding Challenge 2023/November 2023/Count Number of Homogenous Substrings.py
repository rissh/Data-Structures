
class Solution:
    def countHomogenous(self, s: str) -> int:

        n = len(s)
        res = 0
        last = 1
        streak = 0
        mod = 10 ** 9 + 7

        for char in s:
            if char == last:
                streak += 1

            else:
                streak = 1

            last = char
            res += streak 

        return res % mod
      
