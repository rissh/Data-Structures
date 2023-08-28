
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        res = 0
        n = len(mat)

        for i in range(n):
            res += mat[i][i]    #Primary
            res += mat[i][n - 1 - i]    #Secondary


        if n % 2 != 0:
            return res - mat[n // 2][n // 2]
        return res

       # return res - (mat[n // 2][n // 2] if n % 2 else 0)
       
