
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = Counter(nums)
        
        for i in arr:
            if arr[i] > 1:
                return i
              
