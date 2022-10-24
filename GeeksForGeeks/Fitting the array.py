# Method 1
#User function Template for python3

class Solution:
    def isFit (self,arr, brr, n) : 
        #Complete the function
        arr.sort()
        #print(arr)
        brr.sort()
        #print(brr)        
        for i in range(n):
            if arr[i] > brr[i]:
                return False
        return True    
      
# Method 2
#User function Template for python3

class Solution:
    def isFit (self,arr, brr, n) : 
        #Complete the function
        arr.sort()
        brr.sort()
        flag = 0
        for i in range(n):
            if arr[i]>brr[i]:
                flag = -1
                break
            
        if flag != -1:
            return True
        else:
            return False
 
#Method 3
#User function Template for python3

class Solution:
    def isFit (self,arr, brr, n) : 
        #Complete the function
        arr.sort()
        brr.sort()
        count=0
        for i in range(n):
            if arr[i]<=brr[i]:
                count+=1
        if count==n:
            return True
        return False
