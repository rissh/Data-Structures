
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        inc_dp = [1] * n  
        dec_dp = [1] * n  
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc_dp[i] = inc_dp[i - 1] + 1
                
            if nums[i] < nums[i - 1]:
                dec_dp[i] = dec_dp[i - 1] + 1
                
        return max(max(inc_dp), max(dec_dp))
