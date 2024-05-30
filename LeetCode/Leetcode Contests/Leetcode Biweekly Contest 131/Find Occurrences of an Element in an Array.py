
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        n = len(nums)
        m = len(queries)
        indices = [i for i, num in enumerate(nums) if num == x]
    
        res = []
        for query in queries:
            
            if query <= len(indices):
                res.append(indices[query - 1])
                
            else:
                res.append(-1)
    
        return res
        
