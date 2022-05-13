
#User function Template for python3
import heapq
class Solution:
    def maximizeArray(self, arr1, arr2, n):
        # code here
        heap = []
        a = set()
        for i, j in enumerate(arr2+arr1):
            if j not in a:
                heapq.heappush(heap, (j, i))
                a.add(j)
                if len(heap)>n:
                    heapq.heappop(heap)
        return [arr[0] for arr in sorted(heap, key=lambda arr: arr[1])]
        
