
#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
		dict_ = {}
        sumAll = 0
        max_ = 0
        for i in range(n):
            sumAll+=arr[i]
            temp = ((sumAll%K)+K)%K
            
            if(temp == 0):
                max_=i+1
            elif(temp in dict_.keys()):
                if(max_ <(i-dict_[temp])):
                    max_ = i-dict_[temp]
           
            
            else:
                dict_[temp] = i
        return max_
      
