
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        res = [1]

        for i in range(rowIndex):
            Next = [0] * (len(res) + 1)
            for j in range(len(res)):
                Next[j] += res[j]
                Next[j+1] += res[j]

            res = Next

        return res
      
