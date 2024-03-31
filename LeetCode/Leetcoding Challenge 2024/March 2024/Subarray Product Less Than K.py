
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        count = 0
        left = 0
        prod = 1
        n = len(nums)

        for right in range(n):
            prod *= nums[right]

            while  left <= right and prod >= k:
                prod = prod // nums[left]
                left += 1
            count += (right - left + 1)

        return count

