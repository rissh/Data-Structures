
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        mod = 10 ** 9 + 7
        dp = {}

        def count(n, target):

            if n == 0:
                return 1 if target == 0 else 0

            if (n, target) in dp:
                return dp[(n, target)]

            res = 0
            for val in range(1, k + 1):
                res = (res + count(n - 1, target - val)) % mod
            dp[(n, target)] = res

            return res

        return count(n, target)
      
