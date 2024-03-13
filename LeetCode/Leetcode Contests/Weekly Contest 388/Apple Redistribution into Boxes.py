
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        capacity.sort()
        total = sum(apple)
        res, cap = 0, 0
    
        for c in reversed(capacity):
            cap += c
            res += 1
            if cap >= total:
                break
    
        return res
      
