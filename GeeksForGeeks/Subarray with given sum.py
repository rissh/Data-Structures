
#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        j=0
        sum=0
        for i in range(n):
            sum+=arr[i]
            while sum>s and j<i:
                sum-=arr[j]
                j+=1
            if sum==s:
                return [j+1,i+1]
        return [-1]
      
