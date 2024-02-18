
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        position = 0
        res = 0
    
        for step in nums:
            if step < 0:
                position -= abs(step)
            else:
                position += step
        
            if position == 0:
                res += 1
            
        return res
      
