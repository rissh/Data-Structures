# Method - 1
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        if(n == 1):
            return 1
        dp = [nums[i-1]-nums[i] for i in range(1,n) if nums[i-1]-nums[i] != 0]
        
        curr = 2
        
        for i in range(1,len(dp)):
            if(dp[i-1] > 0 and dp[i] < 0) or (dp[i-1] < 0 and dp[i] > 0):
                curr += 1
                
        return curr

# Method - 2
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        f = 1
        d = 1
        
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                f = d+1
            elif nums[i] < nums[i-1]:
                d = f+1
        res = max(f, d)
        
        return res
      
