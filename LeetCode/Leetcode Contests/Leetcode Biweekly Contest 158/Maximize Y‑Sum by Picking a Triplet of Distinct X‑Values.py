
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:

        n = len(x)
        m = len(y)
        res = {}

        for xi, yi in zip(x, y):
            if xi not in res or yi > res[xi]:
                res[xi] = yi

        if len(res) < 3:
            return -1

        top3 = sorted(res.values(), reverse=True)[:3]
        return sum(top3)
        ©leetcode
      
