
#User function Template for python3

import math
class Solution:
    def subsetXOR(self, arr, N, K): 
        # code here
        max_ele = arr[0]
        for i in range(1, N):
            if arr[i] > max_ele :
                max_ele = arr[i]
            
    # Maximum possible XOR value
        m = (1 << (int)(math.log2(max_ele) + 1)) - 1
        if( K > m  ):
           return 0


    # The value of dp[i][j] is the number 
    # of subsets having XOR of their elements 
    # as j from the set arr[0...i-1]

    # Initializing all the values 
    # of dp[i][j] as 0
        dp = [[0 for i in range(m + 1)]
                 for i in range(N + 1)]
    
    # The xor of empty subset is 0
        dp[0][0] = 1

    # Fill the dp table
        for i in range(1, N + 1):
            for j in range(m + 1):
                dp[i][j] = (dp[i - 1][j] + 
                        dp[i - 1][j ^ arr[i - 1]])

    # The answer is the number of subset 
    # from set arr[0..n-1] having XOR of
    # elements as k
        return dp[N][K]
    
