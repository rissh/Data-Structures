
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        mapped = Counter(arr)
        
        i = 0
        for key, count in mapped.items():
            if count == 1:
                i += 1
            
            if i == k:
                return key
            
        return ""
        
