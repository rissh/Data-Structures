
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:

        n = len(A)
        m = len(A[0])
        dp = {}

        def dfs(r, c):
            if r == n:
                return 0

            if c < 0 or c == n:
                return float("inf") 

            if (r, c) in dp:
                return dp[(r, c)]

            res = A[r][c] + min(
                dfs(r + 1, c - 1), 
                dfs(r + 1, c),
                dfs(r + 1, c + 1)
            )

            dp[(r, c)] = res
            return res

        res = float("inf")
        for c in range(n):
            res = min(res, dfs(0, c))

        return res
      
