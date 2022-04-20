
#User function Template for python3
from math import floor, sqrt
import heapq

class Solution:
    def maximumProfit(self, N, C, w, p):
        # Code here
        q = []
        max_profit = 0
        for val in range(N):
            if sqrt(w[val]) == int(sqrt(w[val])):
                continue
            heapq.heappush(q, (-p[val]/w[val], val))
        while C != 0 and len(q):
            ratio, index = heapq.heappop(q)
            ratio = -ratio
            if w[index] <= C:
                C -= w[index]
                max_profit += p[index]
            else:
                max_profit += round(ratio * C,3)
                C = 0
        return max_profit
      
