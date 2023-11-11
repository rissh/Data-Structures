
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = collections.defaultdict(list)
        for edge in edges:
            self.addEdge(edge)
        

    def addEdge(self, edge: List[int]) -> None:
        frm, to, cost = edge
        self.graph[frm].append((to, cost))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        visited = set()

        while heap:
            cost, node = heapq.heappop(heap)
            visited.add(node)

            if node == node2:
                return cost

            for nei, nc in self.graph[node]:
                if nei not in visited:
                    heapq.heappush(heap, (cost + nc, nei))

        return -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
