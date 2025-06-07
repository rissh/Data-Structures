class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        n = len(prices)
        if n == 0 or k == 0:
            return 0

        dp = [[[float('-inf')] * 3 for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0][0] = 0

        for i in range(n):
            for t in range(k+1):
                for h in range(3):
                    if dp[i][t][h] == float('-inf'):
                        continue

                    dp[i+1][t][h] = max(dp[i+1][t][h], dp[i][t][h])

                    if h == 0:
                        if t <= k:
                            dp[i+1][t][1] = max(dp[i+1][t][1], dp[i][t][0] - prices[i])
                            
                        if t <= k:
                            dp[i+1][t][2] = max(dp[i+1][t][2], dp[i][t][0] + prices[i])
                            
                    elif h == 1 and t + 1 <= k:
                        dp[i+1][t+1][0] = max(dp[i+1][t+1][0], dp[i][t][1] + prices[i])
                        
                    elif h == 2 and t + 1 <= k:
                        dp[i+1][t+1][0] = max(dp[i+1][t+1][0], dp[i][t][2] - prices[i])

        return max(dp[n][t][0] for t in range(k+1))
        ©leetcode
