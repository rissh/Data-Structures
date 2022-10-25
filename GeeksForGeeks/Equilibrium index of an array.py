# Method 1
# Your task is to ocomplete this function
# Function should return an integer
def findEquilibrium(a,n):
    # Code here
    leftsum = 0
    rightsum = 0
    
    for i in range(n):
        leftsum = 0
        rightsum = 0
        
        for j in range(i):
            leftsum += arr[j]
            
        for j in range(i+1,n):
            rightsum += arr[j]
            
        if(leftsum == rightsum):
            return i
    return -1 

# Method 2
# Your task is to ocomplete this function
# Function should return an integer
def findEquilibrium(a,n):
    # Code here
    total = sum(arr)
    leftsum = 0
    
    for i, num in enumerate(arr):
        total -= num
 
        if leftsum == total:
            return i
        leftsum += num
        
    return -1
    
# Method 3
# Your task is to ocomplete this function
# Function should return an integer
def findEquilibrium(a,n):
    # Code here
    
    leftsum = []
    rightsum = []
    
    for i in range(n):
        if(i):
            leftsum.append(leftsum[i-1] + arr[i])
            rightsum.append(rightsum[i-1] + arr[n-1-i])
        else:
            leftsum.append(arr[i])
            rightsum.append(arr[n-1-i])
            
    for i in range(n):
        if(leftsum[i] == rightsum[n-1-i]):
            return i
    return -1  
