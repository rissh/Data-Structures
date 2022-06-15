
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        sum1 = 0
        start = 0
        m = 0
        for i in range(len(nums)):
            while nums[i] in s:
                s.remove(nums[start])
                sum1 -= nums[start]
                start += 1
            s.add(nums[i])
            sum1 += nums[i]
            m = max(m,sum1)
        return m
      
