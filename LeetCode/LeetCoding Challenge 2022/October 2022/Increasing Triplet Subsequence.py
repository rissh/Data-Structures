
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        f,s = float('inf'),float('inf')
        
        for i in nums:
            if i <= f:
                f = i
            elif i <= s:
                s = i
            else:
                return True
            
        return False   
      
