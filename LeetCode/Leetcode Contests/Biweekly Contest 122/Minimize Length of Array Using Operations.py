
from math import gcd
from functools import reduce

class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        size = n
        
        if n > 2 and nums[0] != nums[1]:
            return 1

        array_gcd = nums[0]
        i = 1
        while i < n:
            array_gcd = gcd(array_gcd, nums[i])
            i += 1

        res = 0
        j = 0
        while j < n:
            if nums[j] == array_gcd:
                res += 1
            j += 1

        return max(1, (res + 1) // 2)
      
