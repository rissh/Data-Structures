
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        
        n = len(nums)
        hashMap = Counter(nums)
    
        for num in hashMap.values():
            if num > 2:
                return False
            
        return True
      
