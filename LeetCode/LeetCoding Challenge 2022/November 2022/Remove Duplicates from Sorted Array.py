
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1 : return 0
        pos = 0
        for i in range(len(nums)):
            if nums[i] != nums[pos] :
                pos += 1
                nums[pos] = nums[i]
                
        return pos+1
      
