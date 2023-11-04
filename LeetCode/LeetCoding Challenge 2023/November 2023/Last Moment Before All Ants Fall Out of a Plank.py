
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:

        res = 0

        for i in right:
            res = max(n - i, res)

        for i in left:
            res = max(i, res)

        return res

