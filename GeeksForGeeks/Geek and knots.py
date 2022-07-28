
#User function Template for python3
import math
class Solution:
    def knots(self, M, N, K):
        m=max(M,N)
        dp=[0]*(m+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,len(dp)):
            dp[i]=i*dp[i-1]
            
        num1=dp[M]//(dp[M-K]*dp[K])
        num2=dp[N]//(dp[N-K]*dp[K])
        return (num1*num2)%1000000007
      
