
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        n = len(arr)
        arr.sort()
        prev = 0   #for condition --> The value of the first element in arr must be 1.

        for x in arr:
            prev = min(prev + 1, x)
        
        return prev
      
