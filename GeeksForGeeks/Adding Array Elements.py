
import heapq
class Solution:
    def minOperations(self, arr, n, k):
        # code here
        c=0
        heapq.heapify(arr)
        for i in range(n):
            a=heapq.heappop(arr)
            if(a<k):
                b=heapq.heappop(arr)
                d=a+b
                heapq.heappush(arr,d)
                c=c+1
            else:
                break
        return c
      
