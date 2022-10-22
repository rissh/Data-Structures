
#User function Template for python3

class Solution:
    def fillingBucket(self, N):
        # code here
        m=100000000
        dp=[-1 for _ in range(N+1)]
        dp[0]=dp[1]=1
        for i in range(2,N+1):
            dp[i]=(dp[i-1]%m+dp[i-2]%m)%m
        return dp[N]
