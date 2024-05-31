
class Solution:
    def specialArray(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()

        for i in range(n + 1):

            left, right = 0, n - 1

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] < i:
                    left = mid + 1

                else:
                    right = mid - 1

            if n - left == i:
                return n - left

        return -1
        
