
class Solution:
    def MinCoin(self, nums, amt):
        # Code here
        nums.sort()
        n=len(nums)
        dp=[-1 for _ in range(amt+1)]
        dp[0]=0
        for i in range(1,amt+1):
            m=float('inf')
            for j in nums:
                if(j<=i and dp[i-j]!=-1):
                    m=min(dp[i-j]+1,m)
            if(m!=float('inf')):
                dp[i]=m
        return dp[-1]
      
