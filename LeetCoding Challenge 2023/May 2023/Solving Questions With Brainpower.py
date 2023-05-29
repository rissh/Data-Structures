
def f(arr, dp, i, n):
    if(i > n):
        return 0

    if(dp[i] != -1):
        return dp[i]

    solve = arr[i][0] + f(arr, dp, i + arr[i][1] + 1, n)
    skip = 0 + f(arr, dp, i+1, n)
    dp[i] =  max(solve, skip)

    return dp[i]

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n-1, -1, -1):
            skip = min(n, i + questions[i][1] + 1)
            solved = questions[i][0] + dp[skip]
            skiped = dp[i+1]

            dp[i] = max(skiped,solved)

        return dp[0]
        
