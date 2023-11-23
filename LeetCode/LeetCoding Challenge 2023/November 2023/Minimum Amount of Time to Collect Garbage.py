
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        n = len(garbage)
        m = len(travel)

        def cal(x):
            total = 0
            curr = 0

            for i, g in enumerate(garbage):
                if i - 1 >= 0:
                    curr += travel[i - 1]
                
                if x in g:
                    curr += g.count(x)
                    total = curr

            return total

        return cal("P") + cal("M") + cal("G")
      
