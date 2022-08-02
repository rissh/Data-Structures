
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        res = []
        
        for mat in matrix:
            res.extend(mat)
            
        res.sort()
        
        return res[k-1] 
        
