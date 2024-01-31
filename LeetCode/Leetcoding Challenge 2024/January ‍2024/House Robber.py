

def f(ind,arr,dp):

    n = len(arr)
    dp[0] = arr[0]

    for ind in range(1,n):
        pick = arr[ind]
        if(ind>1):
            pick += dp[ind-2]
        non_pick = 0 + dp[ind-1]    
    
        dp[ind] = max(pick,non_pick)
        
    return dp[n-1]

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        #dp = [-1] * (n)
        #return f(n-1,nums,dp)

        prev = nums[0]
        prev2 = 0

        for i in range(1,n):
            pick = nums[i]
            if(i > 1):
                pick += prev2
            
            notPick = 0 + prev

            curr = max(pick,notPick)
            prev2 = prev
            prev = curr

        return prev

