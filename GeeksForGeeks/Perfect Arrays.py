# Method 1
#User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        
        return arr == arr[::-1]

# Method 2
#User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        
        i = 0
        j = n-1
        
        while(i <= j):
            if(arr[i] != arr[j]):
                return False
            i += 1
            j -= 1
        return True   
      
# Method 3
#User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        
        nums = []
        for i in range(n-1,-1,-1):
            nums.append(arr[i])
            
        return nums == arr
      
# Method 4
#User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        
        i = 0 
        for i in range(n):
            if arr[i] != arr[n-i-1]:
                return False
        return True  
