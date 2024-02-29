
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0
        
        for i in range(1, n + 1):
            ans ^= i

        for num in nums:
            ans ^= num

        return ans

        '''
        n = len(nums)
        res = n

        for i in range(n):
            res += (i - nums[i])

        return res
        '''
        '''
        n = len(nums)
        
        for i in range(n+1):
            if i not in nums:
                return i
        '''
      
