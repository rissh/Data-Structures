
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        heapq.heapify(nums)
            
        res = 0
        while nums[0] < k:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            res += 1
            
            val = min(first, second) * 2 + max(first,second)
            heapq.heappush(nums, val)
            
        return res
      
