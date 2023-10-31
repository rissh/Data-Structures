
#User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr, n):
        pos = 0
        
        for i in range(n):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos+=1
              
