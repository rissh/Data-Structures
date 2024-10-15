
import math
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        res = 0
        heapArray = [-x for x in nums]
        n = len(nums)
        
        heapq.heapify(heapArray)
        
        for i in range(k):
            if not heapArray:
                break
                
            max_element = -heapq.heappop(heapArray)
            res += max_element
            heapq.heappush(heapArray, -math.ceil(max_element / 3))

        return res

