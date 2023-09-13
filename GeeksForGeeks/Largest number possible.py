#User function Template for python3

class Solution:
    def findLargest(self, N, S):
        # code here
        
        number = 0
        count = 0
        
        if S==0 and N>1:
            return -1
            
        i = 9
        while(N>0):
            if S>=i:
                number = (number * 10) + i
                S = S - i
                count+=1
                N-=1
            else:
                i = i - 1
                
        
        if S>0:
            return -1
 
            
        return number
                
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, S = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.findLargest(N, S))
# } Driver Code Ends
