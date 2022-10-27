# Method 1
#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,a, n, X):
        # Your Code Here
        
        a.sort()
        for i in range(n):
            c = a[i]
            t = X - c
            l = i + 1
            r = n-1
            while(l < r):
                if(a[l] + a[r] == t):
                    return True
                elif(a[l] + a[r] < t):
                    l += 1
                else:
                    r -= 1
        return False
  
# Method 2
#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        # Your Code Here
        A.sort()
        for i in range(0, n-2):
            l = i + 1
            r = n-1
            while (l < r):
         
                if( A[i] + A[l] + A[r] == X):
                    return True
             
                elif (A[i] + A[l] + A[r] < X):
                    l += 1
                else:
                    r -= 1
        return False 
