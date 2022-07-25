
#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, adj, S):
        #code here
        MAX = 100000000
        dist = [MAX]*V
        dist[S] = 0
        
        # print(dist)
        for i in range(0,V-1):
            for j in range(len(adj)):
                u = adj[j][0]
                v = adj[j][1]
                weight = adj[j][2]
                if(dist[v]>dist[u]+weight):
                    dist[v] = dist[u]+weight
                    
        return dist
        
