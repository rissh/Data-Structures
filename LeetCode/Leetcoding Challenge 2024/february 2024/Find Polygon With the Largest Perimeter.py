
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()
        total = 0
        res = -1

        for n in nums:

            if total > n:
                res = total + n
            total += n

        return res

        '''
        n = len(nums)
        res = 0
        nums.sort()
        pre = [0] * n
        pre[0] = nums[0]

        i = 1

        while i < n:
            pre[i] = pre[i - 1] + nums[i]
            i += 1

        i = 2
        while i < n:
            if nums[i] < pre[i - 1]:
                res = max(res, pre[i])
            i += 1

        if res != 0:
            return res
        else: 
            return -1

        '''
      
