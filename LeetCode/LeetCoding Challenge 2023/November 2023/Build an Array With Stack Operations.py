
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        res = []
        prev = 1

        for i in target:
            while prev != i:
                res.append("Push")
                res.append("Pop")

                prev += 1

            res.append("Push")
            prev += 1

        return res
      
