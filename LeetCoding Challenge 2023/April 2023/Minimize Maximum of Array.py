
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        n = len(nums)
        res = nums[0]
        totalSum = nums[0]

        for i in range(1,n):
            totalSum += nums[i]
            res = max(res,math.ceil(totalSum / (i + 1)))

        return res
        
