
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parents = {}

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
    
        def union(x,y):
            parents.setdefault(x,x)
            parents.setdefault(y,y)

            r1 = find(x)
            r2 = find(y)

            if r1 != r2:
                parents[r2] = r1

        for i,j in stones:
            union(i,~j)
    
        roots = set()
        for key in parents:
            root = find(key)
            roots.add(root)
        return len(stones) - len(roots)
        
