
class Solution(object):
    def __init__(self):
        self.timer = 0
		
    def criticalConnections(self, n, connections):
        low, timeV, visited = [0 for _ in range(n)], [0 for _ in range(n)], [False for _ in range(n)]
        graph = defaultdict(list)
        ans = []
        def tarjan(start, pre):
            visited[start] = True
            timeV[start] = low[start] = self.timer
            self.timer += 1
            for neighbor in graph[start]:
                if neighbor == pre: continue
                if visited[neighbor]:
                    low[start] = min(low[start], timeV[neighbor])
                else:
                    tarjan(neighbor, start)
                    low[start] = min(low[start], low[neighbor])
                    if low[neighbor] > timeV[start]:
                        ans.append([start, neighbor])        

            
        for i in range(len(connections)):
            graph[connections[i][0]].append(connections[i][1])
            graph[connections[i][1]].append(connections[i][0])

        tarjan(0, -1)
        return ans
        
