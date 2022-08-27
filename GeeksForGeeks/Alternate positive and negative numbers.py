
#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        ans=[]
        pos=[]
        neg=[]
        for i in range(len(arr)):
            if arr[i]>=0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        for i in range(n):
            if i%2==0 and pos:
                ans.append(pos.pop(0))
            elif i%2!=0 and neg:
                ans.append(neg.pop(0))
        while pos:
            ans.append(pos.pop(0))
        while neg:
            ans.append(neg.pop(0))
        for i in range(n):
            arr[i]=ans[i]
            
