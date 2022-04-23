
#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        Arr.append(k)
        Arr.sort()
        for i in range(len(Arr)):
            if Arr[i] == k:
                return i
                
