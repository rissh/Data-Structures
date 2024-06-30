
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0
        
        even_dp = [0] * n
        odd_dp = [0] * n
        
        even_dp[0] = 1 if nums[0] % 2 == 0 else 0
        odd_dp[0] = 1 if nums[0] % 2 != 0 else 0
        
        for i in range(1, n):
            if nums[i] % 2 == 0:
                even_dp[i] = odd_dp[i-1] + 1
                odd_dp[i] = odd_dp[i-1]
            else:
                even_dp[i] = even_dp[i-1]
                odd_dp[i] = even_dp[i-1] + 1
        
        res = max(even_dp[n-1], odd_dp[n-1])
        
        even = 0
        odd = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
        
        res = max(res, even, odd)
        
        return res

        
