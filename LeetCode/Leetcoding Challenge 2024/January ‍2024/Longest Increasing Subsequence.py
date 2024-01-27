
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        N = len(arr)
    
        dp = [1]*N    
        for i in range(1, N):
            for j in range(i-1, -1, -1):
                if (1 + dp[j] > dp[i]) and arr[j] < arr[i]:
                    dp[i] = 1 + dp[j]
                    
        return max(dp)
      
