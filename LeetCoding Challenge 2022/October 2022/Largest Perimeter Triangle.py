
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort(reverse = True)
        n=len(nums)
        res = 0
        
        for i in range(n-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                res = nums[i]+nums[i+1]+nums[i+2]
                return res
            
        return 0
      
