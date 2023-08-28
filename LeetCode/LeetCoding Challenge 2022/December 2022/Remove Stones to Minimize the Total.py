
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        def heappush(heap, item):
            """Push item onto heap, maintaining the heap invariant."""
            heap.append(item)
            heapq._siftdown_max(heap, 0, len(heap)-1)

        heapq._heapify_max(piles)
        while k > 0:
            mx = heapq._heappop_max(piles)
            heappush(piles, (mx - (mx // 2)))
            k -= 1
                
        return sum(piles)
        
