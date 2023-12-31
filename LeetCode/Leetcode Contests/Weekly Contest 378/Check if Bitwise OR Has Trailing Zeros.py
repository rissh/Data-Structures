
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                res = nums[i] | nums[j]
                if res & 1 == 0:
                    return True
        return False
      
