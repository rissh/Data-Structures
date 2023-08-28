
class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        
        i, j = 0, len(nums)-1
        
        while i < j:
            x = nums[i]+nums[j]
            
            if x == t: return [i+1,j+1]
            
            elif x > t: j-=1
                
            else: i+=1
              
