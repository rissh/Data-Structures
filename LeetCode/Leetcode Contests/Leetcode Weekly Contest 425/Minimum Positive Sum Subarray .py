
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        n = len(nums)
        minSum = float('inf')  
        found = False  
        
        for i in range(n):
            currSum = 0  

            for j in range(i, min(i + r, n)):
                currSum += nums[j]

                if l <= j - i + 1 <= r and currSum > 0:
                    minSum = min(minSum, currSum)
                    found = True

        return minSum if found else -1
        
