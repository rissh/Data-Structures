
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        n = len(mat)
        m = len(mat[0])
        
        rowSum = [0] * n
        colSum = [0] * m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rowSum[i] += 1
                    colSum[j] += 1
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and rowSum[i] == 1 and colSum[j] == 1:
                    ans += 1

        return ans

        # TC -> m * n
        # SC -> m + n
      
