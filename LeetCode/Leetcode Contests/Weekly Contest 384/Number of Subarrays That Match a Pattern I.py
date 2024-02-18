

def f(nums, pattern, start):
    
    for i in range(len(pattern)):
        if pattern[i] == 1 and nums[start + i + 1] <= nums[start + i]:
            return False
        elif pattern[i] == 0 and nums[start + i + 1] != nums[start + i]:
            return False
        elif pattern[i] == -1 and nums[start + i + 1] >= nums[start + i]:
            return False
    return True

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
        n = len(nums)
        m = len(pattern)

        count = 0

        for i in range(n - m):
            if f(nums, pattern, i):
                count += 1

        return count
      
