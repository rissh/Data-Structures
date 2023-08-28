
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        priority_queue = []
        
        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            
            if diff > 0:
                heapq.heappush(priority_queue, diff)
                
                if len(priority_queue) > ladders:
                    bricks -= heapq.heappop(priority_queue)
                
                if bricks < 0:
                    return i
                    
        return len(heights) - 1
      
