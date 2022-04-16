
import sys
class Solution:
	def solveWordWrap(self, nums, k):
		#Code here
		n = len(nums)
        dp = [0] * n
        ans = [0] * n
        dp[n - 1] = 0
        ans[n-1] = n-1
        
        for i in range(n-2, -1,-1):
            currlen = -1
            dp[i] = sys.maxsize
            for j in range(i, n):
                currlen += (nums[j] + 1)
                if currlen > k:
                    break
                if j  == n - 1:
                    cost = 0
                else:
                    cost = ((k - currlen)*(k - currlen) + dp[j + 1])
                if cost < dp[i]:
                    dp[i] = cost
                    ans[i] = j
        
        i = 0
        res = 0
        while i < n:
            pos = 0
            for j in range(i, ans[i] + 1):
                pos = pos + nums[j]
            x = ans[i] - i 
            if ans[i] + 1 != n:
                res = res + (k - x - pos)**2
            i = ans[i] + 1
        return res
      
