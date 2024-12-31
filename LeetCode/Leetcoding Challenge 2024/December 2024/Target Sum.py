
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)

        @cache
        def f(ind, curr):
            if ind == n:
                if curr == target:
                    return 1
                return 0

            total = 0
            total += f(ind + 1, curr + nums[ind])
            total += f(ind + 1, curr - nums[ind])

            return total

        return f(0, 0)
        
