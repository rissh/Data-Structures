
class Solution:
	def sortedArrayToBST(self, nums):
        s=0
        e=len(nums)-1
        root=self.makingtree(nums,s,e,[])
        return root
    def makingtree(self,nums,s,e,ans):
        if(s>e):
            return 
        mid=(s+e)//2
        root=(nums[mid])
        ans.append(root)
        self.makingtree(nums,s,mid-1,ans)
        self.makingtree(nums,mid+1,e,ans)
        return ans
	    # code here
      
