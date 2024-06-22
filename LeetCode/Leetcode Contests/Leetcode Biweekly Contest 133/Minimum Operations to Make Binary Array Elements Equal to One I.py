
def f(nums, x):
    for i in range(3):
        nums[x + i] = 1 - nums[x + i]

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
    
        for i in range(n - 2):
            if nums[i] == 0:
                f(nums, i)
                res += 1
                
        if sum(nums) == n:
            return res 
        else:
            return -1
          
