
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

        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                nums[i] = 1
            elif nums[i + 1] < nums[i]:
                nums[i] = -1
            else:
                nums[i] = 0
        nums[-1] = 2
        
        lps = [0] * m
        i = 1
        j = 0
        while i < m:
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        res = 0
        i = j = 0
        while (n - i) >= (m - j):
            if pattern[j] == nums[i]:
                j += 1
                i += 1
            if j == m:
                res += 1
                j = lps[j - 1]
            elif i < n and pattern[j] != nums[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return res
      
