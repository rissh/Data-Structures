
def f(ind,T,Arr,dp):
    if (ind==0):
        if T%Arr[0] == 0:
            return 1
        return 0
    if (dp[ind][T] != -1):
        return dp[ind][T]
    
    notTake = f(ind-1,T,Arr,dp)
    take = 0
    if(Arr[ind] <= T):
        take = f(ind,T-Arr[ind],Arr,dp)
        
    dp[ind][T] = take+notTake    
    return dp[ind][T]  

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        dp = [[0 for j in range(amount+1)] for i in range(n)]
        #return f(n-1,amount,coins,dp)
        
        S=coins
        m=amount
        n=len(coins)
        
        dp=[[0 for i in range(m+ 1)] for j in range(n + 1)]
        dp[0][0]=1
        for i in range(1,n+1):
            dp[i][0]=1
        for j in range(1,m+1):
            dp[0][j]=0
                
       
        for i in range(1,n+1):
            for j in range(1,m+1):
                if S[i-1]<=j:
                    dp[i][j]=dp[i][j-S[i-1]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][m]
