
#User function Template for python3

class Solution:
    def dfs(self, inputS, outputS, index, ans):
        if index == len(inputS):
            ans.append(outputS)
            return 
        
        if index != 0:
            self.dfs(inputS, outputS + ' ' + inputS[index], index+1, ans)
        self.dfs(inputS, outputS + inputS[index], index+1, ans)
        
    def permutation (self, S):
        ans = []
        self.dfs(S, '', 0, ans)
        return ans
      
