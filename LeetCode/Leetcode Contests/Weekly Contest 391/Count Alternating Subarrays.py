
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 1
        res = 0

        left = 0
        for right in range(1, n):
            if nums[right] != nums[right - 1]:
                count += 1
            else:
                res += (count * (count + 1)) // 2
                count = 1

        res += (count * (count + 1)) // 2

        return res
        
