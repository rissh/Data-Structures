
class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        
        N = len(arr)
        cnt = [1]*N
        dp = [1]*N 
        
        for i in range(1, N):
            for j in range(i-1, -1, -1):
                if (1 + dp[j] > dp[i]) and arr[j] < arr[i]:
                    dp[i] = 1 + dp[j]
                    cnt[i] = cnt[j]
                elif(arr[i]>arr[j] and dp[i] == dp[j]+1):
                    cnt[i] += cnt[j]
                    
                    
                    
        LisLen = max(dp)
        
        ans = 0
        for i in range(N):
            if(dp[i] == LisLen):
                ans += cnt[i]
        return ans  
