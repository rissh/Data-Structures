
from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        arr = SortedList()
        res = []
        
        for num in nums[::-1]:
            x = SortedList.bisect_left(arr,num)
            res.append(x)
            arr.add(num)
        return reversed(res) 
      
