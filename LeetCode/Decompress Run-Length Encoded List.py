# Method 1
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(0,len(nums),2):
            res.extend(nums[i]*[nums[i+1]])
            
        return res
      
# Method 2
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        i,j=0,1
        ans=[]
        while j<len(nums):
            temp=[nums[j]]*nums[i]
            ans+=temp
            i+=2
            j+=2
        return ans
      
# Method 3
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        ans = []
        for i in range(0,len(nums),2):
            ans += [nums[i+1]]*nums[i]
        return ans
        
