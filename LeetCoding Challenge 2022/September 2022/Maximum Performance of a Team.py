
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        mod = 10 ** 9 + 7
        
        combo = list(zip(speed, efficiency))
        combo.sort(key = lambda x: x[1])
        heap = []
        cur = 0
        last = 0
        res = 0
        
        for i in range(len(combo) - 1, -1, -1):
            speed, eff = combo[i]
            
            if len(heap) >= k - 1:
                if heap and last > heap[0]:
                    cur -= heappop(heap)
                    cur += last
                    heappush(heap, last)
                
            else:
                heappush(heap, last)
                cur += last
            last = speed
            res = max(res, (cur + speed) * eff)
        
        return res % mod
      
