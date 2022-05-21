
#User function Template for python3

class Solution:
    def farNumber(self,N,Arr):
        #code here
        res=[-1]*N
        for i in range(N):
            for j in range(N-1,i,-1):
                if Arr[j]<Arr[i]:
                    res[i]=j
                    break
        return res
      
