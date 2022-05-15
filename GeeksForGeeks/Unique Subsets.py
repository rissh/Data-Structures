
#User function Template for python3

class Solution:
    
    def AllSubsets(self, arr,n):
        #code here
        if len(arr) == 0:
            return []
        arr.sort()
        subset = []
        result = []
        taken = [False for ele in arr]
        result.append([])
        for i in range(len(arr)):
            if i == 0:
                taken[i] = True
                subset.append(arr[i])
                result.append(subset.copy())
                self.dfs(i+1, taken, arr, subset, result)
                del subset[-1]
            else:
                if arr[i-1] == arr[i]:
                    continue
                else:
                    taken[i] = True
                    subset.append(arr[i])
                    result.append(subset.copy())
                    self.dfs(i+1, taken, arr, subset, result)
                    del subset[-1]
        return result
    
    def dfs(self, index, taken, arr, subset, result):
        if index == len(arr):
            return 
        # take index
        if arr[index] == arr[index-1] and taken[index-1] == False:
            self.dfs(index + 1, taken, arr, subset, result)
        else:
            taken[index] = True
            subset.append(arr[index])
            result.append(subset.copy())
            self.dfs(index + 1, taken, arr, subset, result)
            taken[index] = False
            del subset[-1]
            self.dfs(index + 1, taken, arr, subset, result)
    
        
    def appendSortedSubset(self, subset, result):
        subset.sort()
        result.append(subset.copy())
        
