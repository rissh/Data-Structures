
class Solution:
    def numberOfMatches(self, n: int) -> int:

        return n - 1
        res = 0

        while n > 1:
            res += n // 2
            n = math.ceil(n / 2)

        return res
      
