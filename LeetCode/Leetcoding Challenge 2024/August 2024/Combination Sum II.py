
def Csum(ind,target,arr,ans,ds):    #Picking subsequence method
    if(target == 0):    #Base condition
        ans.append(ds.copy())
        return
    for i in range(ind,len(arr)):
        if(i>ind and arr[i]==arr[i-1]):
            continue
        if(arr[i] > target):
            break
        ds.append(arr[i])
        Csum(i+1,target-arr[i],arr,ans,ds)  #Recursion function call
        ds.pop()


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        cadidates = candidates.sort()   #Sort the given array 
        Csum(0,target,candidates,ans,ds)    #Function call
        return ans
        
