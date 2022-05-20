
#User function Template for python3

class Solution:
    def findTime(self, S1, S2):
        # code here 
        arr = [0]
        count = 0
        for i in S2:
            arr.append(S1.index(i))
        for i in range(1,len(arr)):
            count += (abs(arr[i]-arr[i-1]))
        return count
      
