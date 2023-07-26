
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            
            mid = (right + left) // 2

            if (arr[mid-1] < arr[mid]) and (arr[mid] > arr[mid+1]):
                
                # in this way, mid is the peak of the mountain
                return mid
            
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                
                # if true, peak should be on the right hand side
                left = mid
            
            else:
                
                # if true, peak should be on the left hand side
                right = mid
        
        return -1
