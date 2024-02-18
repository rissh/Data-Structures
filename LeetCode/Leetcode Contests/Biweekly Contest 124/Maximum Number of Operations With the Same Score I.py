
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0
        preSum = nums[0] + nums[1]
        ans += 1
        for i in range(2, n - 1, 2):
            
            if preSum == nums[i] + nums[i + 1]:
                ans += 1
            else:
                break
                
        return ans
      
