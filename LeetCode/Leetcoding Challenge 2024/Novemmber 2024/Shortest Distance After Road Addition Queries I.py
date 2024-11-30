
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        #construct graph
        adj = [[] for _ in range(n)]
        for i in range(n-1):
            adj[i].append(i+1)

        res = []
        for i,j in queries:
            adj[i].append(j) #add the edge to graph
            res.append(self.bellman(adj))
            
        return res
    
    def bellman(self, adj):
        n = len(adj)
        dist = [float('inf')]*n
        dist[0] = 0

        # cycle not possible since queries[i][0] < queries[i][1], 
        # so relax only 1 time 
        for u in range(n):
            for v in adj[u]:
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
        
        return dist[-1]
