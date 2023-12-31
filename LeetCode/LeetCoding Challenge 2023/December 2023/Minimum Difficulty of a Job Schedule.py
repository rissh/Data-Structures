
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        n = len(jobDifficulty)
        dp = [[float('inf') for _ in range(d + 1)] for _ in range(n + 1)]
        dp[0][0] = 0

        # dp[i][j] = min(dp[][j-1]) for k [0, i]

        for i in range(1, n + 1):
            
            for j in range(1, d + 1):
                cur_max = 0

                for k in range(i, j-1, -1):

                    cur_max = max(cur_max, jobDifficulty[k-1])
                    dp[i][j] = min(dp[i][j], dp[k-1][j-1] + cur_max)

        #print(dp)
        return dp[n][d] if dp[n][d] < float('inf') else -1
      
