
import heapq
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        n = len(nums)
        heap = []
        res = 0
        count = 0
        
        for i in range(1, n, 2):
            heapq.heappush(heap, nums[i])
            count += 1
            if count == n // 3:
                break
                
        return sum(heap)
      
