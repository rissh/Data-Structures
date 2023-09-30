
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        n = len(nums)
        increase, decrease = True, True

        for i in range(n-1):
            if not(nums[i] <= nums[i + 1]):
                increase = False

            if not(nums[i] >= nums[i + 1]):
                decrease = False

        return increase or decrease
      
