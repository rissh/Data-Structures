
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def dfs(node):
            node_char = s[node]            
            longest = second_longest = 0
            for child in children[node]:
                child_path = dfs(child)
                if s[child] != node_char:                    
                    if child_path >= longest:
                        second_longest = longest
                        longest = child_path 
                    elif child_path > second_longest:
                        second_longest = child_path
                        
            self.result = max(self.result, 1 + longest + second_longest)        
            return 1 + longest
        
        children = defaultdict(list)
        for n in range(1, len(parent)):
            children[parent[n]].append(n)
            
        self.result = 0
        dfs(0)
        
        return self.result
        
