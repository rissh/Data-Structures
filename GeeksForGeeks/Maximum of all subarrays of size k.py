
#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        res = []
        d = deque()
    
        for i in range(k):
            while len(d) and arr[i]>=arr[d[-1]]:
                d.pop()
            d.append(i)
    
        for i in range(k,n):
            
            res.append (arr[d[0]])
            while len(d) and d[0]<=i-k:
                d.popleft()
            while len(d) and arr[i]>=arr[d[-1]]:
                d.pop()
            d.append(i)
    
        res.append (arr[d[0]])
        d.popleft()
        return res
        
        #code here

