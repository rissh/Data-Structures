
def Set(ind,arr,ans,ds):

    n = len(arr)

    if(ind>=n):
        ans.append(ds.copy())
        return

    ds.append(arr[ind])
    Set(ind+1,arr,ans,ds)

    ds.pop()
    Set(ind+1,arr,ans,ds)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        ds = []
        
        Set(0,nums,ans,ds)
        return ans

