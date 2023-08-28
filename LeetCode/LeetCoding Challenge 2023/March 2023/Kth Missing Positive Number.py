
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        n = len(arr)
        i,j = 0,1
        skip = 0
        while(i<n):
            if(arr[i]!=j):
                skip += 1
                if(k==skip):
                    return j
                j += 1
            else:
                i += 1
                j += 1
        return arr[-1]+(k-skip)
        
