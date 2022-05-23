
#User function Template for python3
from collections import deque
class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        pre = prerequisites
        index = [0 for i in range(n)]
        adj = [[] for i in range(n)]
        
        for i in pre:
           index[i[0]] += 1
           adj[i[1]].append(i[0])
           
        q = deque()
        for i in range(n):
           if index[i] == 0:
               q.append(i)
               
        order = []
        temp = 0
        
        while len(q):
           node = q.popleft()
           order.append(node)
           temp = temp+1
           for cur in adj[node]:
               index[cur] = index[cur]-1
               if index[cur] == 0:
                   q.append(cur)
                   
        if temp == n:
           return order
           
        return []
      
