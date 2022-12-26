
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        x=defaultdict(list)
        for n, m in edges:
            x[n].append(m)
            x[m].append(n)
        y,z=deque([source]),set([source])
        while y:
            node=y.popleft()            
            if node==destination:
                return True            
            for i in x[node]:
                if i not in z:
                    z.add(i)
                    y.append(i)
        return False
        
