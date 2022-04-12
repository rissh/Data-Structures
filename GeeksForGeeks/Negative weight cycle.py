
#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		dis=[float('inf')]*n
        dis[0]=0
        for i in range(n-1):
            visited=False
            for i,j,k in edges:
                if dis[j]>dis[i]+k:
                    dis[j]=dis[i]+k
                    visited=True
            if not visited:
                return 0
        for i,j,k in edges:
            if dis[j]>dis[i]+k:
                return 1
        return 0
      
