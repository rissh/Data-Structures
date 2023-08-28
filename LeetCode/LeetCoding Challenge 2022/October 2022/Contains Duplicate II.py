
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and i-seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False
 ##
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        x = {}
        for i in range(len(nums)):
            if nums[i] in x:
                if i - x[nums[i]] <= k:
                    return True
                else:
                    x[nums[i]] = i
            else:
                x[nums[i]] = i
                
        return False
