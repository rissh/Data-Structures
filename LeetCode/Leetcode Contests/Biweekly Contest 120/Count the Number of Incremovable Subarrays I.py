
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0
        i = 0
        
        while i < n:
            j = i
            while j < n:
                remain = nums[:i] + nums[j + 1:]
                increasing = True
                for k in range(len(remain) - 1):
                    if remain[k] >= remain[k + 1]:
                        increasing = False
                        break

                if increasing:
                    count += 1
                j += 1
            i += 1
                    
        return count
      
