
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums = sorted(nums)
        diff = nums[-1] - nums[0]
        # change first three or last three
        diff = min(nums[-1] - nums[3], nums[-4] - nums[0])
        
        # change first two and last one
        diff = min(nums[-2] - nums[2], diff)
        
        # change first and last two
        diff = min(nums[-3] - nums[1], diff)
        
        return diff
        
