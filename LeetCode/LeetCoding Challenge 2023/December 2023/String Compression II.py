
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = {}
        n = len(s)

        def count(i, k, prev, prev_cnt):
            if (i, k, prev, prev_cnt) in dp:
                return dp[(i, k, prev, prev_cnt)]

            if k < 0:
                return float("inf")

            if i == n:
                return 0

            if s[i] == prev:
                incr = 1 if prev_cnt in [1, 9, 99] else 0
                res = incr + count(i + 1, k, prev, prev_cnt + 1)
                
            else:
                res = 1 + count(i + 1, k, s[i], 1)
                res = min(res, count(i + 1, k - 1, prev, prev_cnt))

            dp[(i, k, prev, prev_cnt)] = res
            return res

        return count(0, k, "", 0)
      
